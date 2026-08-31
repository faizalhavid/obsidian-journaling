import os
import pytest


# ---------------------------------------------------------------------------
# Slice 1 — is_authenticated(url) -> bool
# ---------------------------------------------------------------------------

class TestIsAuthenticated:
    def test_returns_true_for_lms_dashboard(self):
        from core.services.scraper import is_authenticated
        assert is_authenticated("https://lms.binus.ac.id/lms/dashboard") is True

    def test_returns_false_when_url_contains_login(self):
        from core.services.scraper import is_authenticated
        assert is_authenticated("https://lms.binus.ac.id/login?continue=%2Flms%2Fdashboard") is False

    def test_returns_false_for_microsoft_sso_redirect(self):
        from core.services.scraper import is_authenticated
        assert is_authenticated("https://login.microsoftonline.com/3485b963-82ba-4a6f-810f-b5cc226ff898/oauth2/v2.0/authorize") is False

    def test_returns_true_for_binusmaya_dashboard(self):
        from core.services.scraper import is_authenticated
        assert is_authenticated("https://binusmaya.binus.ac.id/") is True


# ---------------------------------------------------------------------------
# Slice 2 — session file helpers
# ---------------------------------------------------------------------------

class TestSessionFile:
    def test_session_exists_returns_false_when_no_file(self, monkeypatch, tmp_path):
        monkeypatch.setenv("SESSION_FILE", str(tmp_path / "missing.json"))
        from core.services import scraper
        assert scraper.session_exists() is False

    def test_session_exists_returns_true_when_file_present(self, monkeypatch, tmp_path):
        f = tmp_path / "session.json"
        f.write_text('{"cookies": [], "origins": []}')
        monkeypatch.setenv("SESSION_FILE", str(f))
        from core.services import scraper
        assert scraper.session_exists() is True

    def test_get_session_file_defaults_to_sessions_folder(self, monkeypatch):
        from pathlib import Path
        monkeypatch.delenv("SESSION_FILE", raising=False)
        from core.services import scraper
        assert scraper.get_session_file() == Path(".sessions/binus_session.json")

    def test_get_session_file_uses_env_override(self, monkeypatch, tmp_path):
        from pathlib import Path
        custom = str(tmp_path / "custom.json")
        monkeypatch.setenv("SESSION_FILE", custom)
        from core.services import scraper
        assert scraper.get_session_file() == Path(custom)


# ---------------------------------------------------------------------------
# Slice 3 — authenticate() end-to-end (integration, needs live LMS + creds)
# ---------------------------------------------------------------------------

class TestRequireCredentials:
    def test_raises_environment_error_when_username_missing(self, monkeypatch):
        monkeypatch.delenv("BINUS_USERNAME", raising=False)
        monkeypatch.setenv("BINUS_PASSWORD", "somepassword")
        from core.services.scraper import _require_credentials
        with pytest.raises(EnvironmentError, match="BINUS_USERNAME"):
            _require_credentials()

    def test_raises_environment_error_when_password_missing(self, monkeypatch):
        monkeypatch.setenv("BINUS_USERNAME", "user@binus.ac.id")
        monkeypatch.delenv("BINUS_PASSWORD", raising=False)
        from core.services.scraper import _require_credentials
        with pytest.raises(EnvironmentError, match="BINUS_PASSWORD"):
            _require_credentials()

    def test_passes_when_both_credentials_present(self, monkeypatch):
        monkeypatch.setenv("BINUS_USERNAME", "user@binus.ac.id")
        monkeypatch.setenv("BINUS_PASSWORD", "secret")
        from core.services.scraper import _require_credentials
        _require_credentials()  # should not raise


@pytest.mark.integration
class TestAuthenticate:
    def test_returns_login_session_on_lms_dashboard(self):
        if not os.getenv("BINUS_USERNAME"):
            pytest.skip("BINUS_USERNAME not set — skipping live login test")

        from core.services.scraper import authenticate, LMS_URL
        session = authenticate()
        try:
            assert "binusmaya.binus.ac.id" in session.page.url or LMS_URL in session.page.url
        finally:
            session.close()

    def test_saves_session_file_after_login(self, monkeypatch, tmp_path):
        if not os.getenv("BINUS_USERNAME"):
            pytest.skip("BINUS_USERNAME not set — skipping live login test")

        session_file = tmp_path / "test_session.json"
        monkeypatch.setenv("SESSION_FILE", str(session_file))

        from core.services.scraper import authenticate
        session = authenticate()
        try:
            assert session_file.exists(), "Session file was not saved after login"
        finally:
            session.close()
