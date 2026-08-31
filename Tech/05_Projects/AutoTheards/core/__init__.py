import os
import click
from flask import Flask

from core.routes import bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-change-me")

    app.register_blueprint(bp)

    @app.cli.command("scrape")
    def scrape_command() -> None:
        """Run the Binus LMS scraper: login, scrape todos, store in SQLite."""
        from core.services.scraper import authenticate
        print("Starting LMS scrape...")
        session = authenticate()
        try:
            # Scraping logic goes here (next spec)
            print("Login successful. Scraping not yet implemented.")
        finally:
            session.close()
            click.echo("Done.")

    return app
