from pprint import pprint
import requests

TEST_VEHICLE_DATA = {
    "license_plate": "SDF312MVNS",
    "v_type": "Van",
    "color": "White",
    "parking_spot_no": "2",
    "description": "Updated discription",
    "user_id": "3"
}

URL = "http://127.0.0.1:5000/vehicle/1"

def update_vehicle():
    out = requests.put(URL, json=TEST_VEHICLE_DATA)
    if out.status_code == 200:
        pprint (out.json())
    else:
        print("Something went wrong while trying to update.")


if __name__ == "__main__":
    update_vehicle()