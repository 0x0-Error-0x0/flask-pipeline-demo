from flask import Blueprint, jsonify, current_app

bp = Blueprint("main", __name__)

@bp.get("/")
def root():
    return jsonify(status="ok", message="Hello from clean Flask project!")

@bp.get("/notes")
def notes():
    try:
        with open(current_app.config["DATA_FILE"], "r", encoding="utf-8") as f:
            content = f.read().strip()
    except FileNotFoundError:
        content = ""
    return jsonify(notes=content)
