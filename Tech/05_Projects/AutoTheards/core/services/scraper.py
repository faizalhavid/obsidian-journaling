import os
from pathlib import Path
from typing import NamedTuple

from playwright.sync_api import Page, Playwright, sync_playwright

LMS_URL = "https://lms.binus.ac.id/lms/dashboard"
_CODEGEN_HINT = (
    "\nLogin failed. To re-record the login flow, run:\n"
    "  playwright codegen {lms_url} --save-storage={session_file}\n"
    "Then re-run `flask scrape`."
)


class LoginSession(NamedTuple):
    """
    Holds the authenticated Page and the Playwright instance.
    Caller must call close() when done to release all browser resources.
    """
    page: Page
    playwright: Playwright

    def close(self) -> None:
        try:
            self.page.context.browser.close()
        finally:
            self.playwright.stop()


def is_authenticated(url: str) -> bool:
    return "/login" not in url and "microsoftonline.com" not in url


def get_session_file() -> Path:
    return Path(os.getenv("SESSION_FILE", ".sessions/binus_session.json"))


def session_exists() -> bool:
    return get_session_file().exists()


def authenticate() -> LoginSession:
    """
    Opens a headed Chromium browser, logs in to the Binus LMS via Microsoft SSO,
    handles both post-login modals, saves the session, and returns a LoginSession.

    Call session.close() when done to release browser and Playwright resources.
    """
    _require_credentials()

    username = os.environ["BINUS_USERNAME"]
    password = os.environ["BINUS_PASSWORD"]
    session_path = get_session_file()

    print("[1/6] Starting Playwright (headed)...")
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=False)

    print("[2/6] Setting up browser context...")
    if session_exists():
        print("      Loading saved session from", session_path)
        context = browser.new_context(storage_state=str(session_path))
    else:
        print("      No saved session found — starting fresh.")
        context = browser.new_context()

    page = context.new_page()

    try:
        print("[3/6] Navigating to LMS dashboard...")
        page.goto(LMS_URL, wait_until="networkidle")

        if not is_authenticated(page.url):
            print("[4/6] Session expired or absent — logging in via Microsoft SSO...")
            _do_sso_login(page, username, password)
            print("      SSO login complete.")
        else:
            print("[4/6] Session valid — skipping login.")

        print("[5/6] Handling post-login modals...")
        _handle_modals(page)

        print("[6/6] Saving session to disk...")
        session_path.parent.mkdir(parents=True, exist_ok=True)
        context.storage_state(path=str(session_path))

        print(f"\nAuthenticated. Current URL: {page.url}")
        return LoginSession(page=page, playwright=pw)

    except Exception as exc:
        try:
            page.screenshot(path="error_screenshot.png")
            print("\nerror_screenshot.png saved.")
        except Exception:
            pass
        try:
            browser.close()
            pw.stop()
        except Exception:
            pass
        print(_CODEGEN_HINT.format(lms_url=LMS_URL, session_file=session_path))
        raise RuntimeError("Login failed — see error_screenshot.png") from exc


def _require_credentials() -> None:
    missing = [v for v in ("BINUS_USERNAME", "BINUS_PASSWORD") if not os.getenv(v)]
    if missing:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing)}. "
            "Copy .env.example to .env and fill in your credentials."
        )


def _do_sso_login(page: Page, username: str, password: str) -> None:
    # Microsoft email step
    page.fill('input[type="email"]', username)
    page.click('input[type="submit"]')
    page.wait_for_load_state("networkidle")

    # Password step
    page.fill('input[type="password"]', password)
    page.click('input[type="submit"]')

    # Wait for redirect back to Binus — accepts either domain in the flow
    page.wait_for_url(
        lambda url: "binusmaya.binus.ac.id" in url or "lms.binus.ac.id" in url,
        timeout=30_000,
    )


def _handle_modals(page: Page) -> None:
    # Modal 1 (always present): confirm redirect to LMS
    # Selectors are best-guess — verify/update with: playwright codegen <LMS_URL>
    _wait_and_click(page, "button:has-text('OK'), button:has-text('Lanjut'), button:has-text('Continue')", label="modal-1 (redirect confirm)")
    page.wait_for_load_state("networkidle")

    # Modal 2 (always present): close welcome / new-user alert
    _wait_and_click(page, "button:has-text('Close'), button:has-text('Tutup'), [aria-label='Close']", label="modal-2 (welcome close)")
    page.wait_for_load_state("networkidle")


def _wait_and_click(page: Page, selector: str, label: str, timeout: int = 10_000) -> None:
    try:
        page.wait_for_selector(selector, timeout=timeout)
        page.locator(selector).first.click()
    except Exception:
        print(f"      Warning: {label} not found — skipping.")
