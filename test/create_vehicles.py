from pprint import pprint
import requests

TEST_VEHICLE = {
    "license_plate": "ASL45TBS1",
    "v_type": "Car",
    "color": "Black",
    "parking_spot_no": "9",
    "description": "Description",
    "user_id": "1"
}

URL = "http://127.0.0.1:5000/vehicles"


def test_vehicle_creation():
    out = requests.post(URL, json=TEST_VEHICLE)
    if out.status_code == 201:
        out_json = out.json()
        pprint(out_json)
        return out_json["new_id"]
    else:
        print("Something went wrong while creating a vehicle.")
        return -1


if __name__ == "__main__":
    new_id = test_vehicle_creation()
