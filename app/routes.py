from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

from app.database import user


@app.route("/")
def version():
    out = {
        "ok": True,
        "message": "Success",
        "server_time": datetime.now().strftime("%F %H:%M:%S"),
        "version": "1.0.0"
    }
    return out

@app.route("/users", methods=["POST"])
def create_user():
    user_data = request.json
    out = {
        "ok": True,
        "message": "Success",
        "new_id": user.insert(
            user_data.get("first_name"),
            user_data.get("last_name"),
            user_data.get("hobbies")
        )
    }

    if not first_name in user_data.get:
        return abort(400, "First name is required")

    return out, 201


@app.route("/users", methods=["GET"])
def get_all_users():
    out = {
        "ok": True,
        "message": "Success",
        "users": user.scan()
    }
    return out



@app.route("/users/<int:pk>", methods=["GET"])
def get_single_user(pk):
    out = {
        "ok": True,
        "message": "Success",
        "user": user.read(pk)
    }

    return out


@app.route("/users/<int:pk>", methods=["PUT"])
def update_user(pk):
    user_data = request.json
    out = {
        "ok": True,
        "message": "Success"
    }

    user.update(pk ,
    user_data.get("first_name"),
    user_data.get("last_name"),
    user_data.get("hobbies"))
    return out


@app.route("/users/<int:pk>", methods=["DELETE"])
def deactivate_user(pk):
    user.deactivate_user(pk)
    out = {
        "ok": True,
        "message": "success"
    }
    return out

