from app.database import vehicle
from app.database import user
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


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
    return out, 201


@app.route("/get/users", methods=["GET"])
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

    user.update(pk,
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

# Vehicle Routes

@app.route("/vehicles", methods=["POST"])
def create_vehicle():
    vehicle_data = request.json
    out = {
        "ok": True,
        "message": "Success",
        "new_id": vehicle.insert(
            vehicle_data.get("license_plate"),
            vehicle_data.get("v_type"),
            vehicle_data.get("color"),
            vehicle_data.get("parking_spot_no"),
            vehicle_data.get("description"),
            vehicle_data.get("user_id"),
        )
    }
    return out, 201


@app.route("/vehicles", methods=["GET"])
def get_all_vehicles():
    out = {
        "ok": True,
        "message": "Success",
        "users": vehicle.scan()
    }
    return out

@app.route("/vehicles/<int:pk>", methods=["GET"])
def get_single_vehicle(pk):
    out = {
        "ok": True,
        "message": "Success",
        "vehicle": vehicle.read(pk)
    }

    return out


@app.route("/vehicles/<int:pk>", methods=["PUT"])
def update_vehicle(pk):
    vehicle_data = request.json
    out = {
        "ok": True,
        "message": "Success"
    }

    vehicle.update(pk,
                vehicle_data.get("license_plate"),
                vehicle_data.get("v_type"),
                vehicle_data.get("color"),
                vehicle_data.get("parking_spot_no"),
                vehicle_data.get("description"),
                vehicle_data.get("user_id")
                )
    return out













