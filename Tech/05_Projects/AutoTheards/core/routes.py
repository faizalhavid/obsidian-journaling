from flask import Blueprint, jsonify

bp = Blueprint("core", __name__)


@bp.get("/health")
def health():
    return jsonify({"status": "ok"})


@bp.get("/todos")
def get_todos():
    # Will query SQLite once scraping is implemented
    return jsonify({"todos": [], "message": "Scraping not yet implemented."})


@bp.get("/todos/new")
def get_new_todos():
    return jsonify({"new_todos": [], "message": "Scraping not yet implemented."})
