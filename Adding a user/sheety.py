import requests
import os

SHEETY_ENDPOINT = "https://api.sheety.co/52c2de514e0e14e040248ee2b2dcaf46/flightDeals/users"
USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']
AUTH = (USERNAME, PASSWORD)


def post_new_row(first_name, last_name, email_address):
    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email_address,
        }
    }
    response = requests.post(url=SHEETY_ENDPOINT, auth=AUTH, json=body)
    response.raise_for_status()
    print(response.text)
