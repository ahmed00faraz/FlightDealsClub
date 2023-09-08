import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/52c2de514e0e14e040248ee2b2dcaf46/flightDeals/prices"
SHEETY_CUSTOMER_ENDPOINT = "https://api.sheety.co/52c2de514e0e14e040248ee2b2dcaf46/flightDeals/users"

USERNAME = "Your Credentials"
PASSWORD = "Your Credentials"

AUTH = (USERNAME, PASSWORD)


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=AUTH)
        self.destination_data = response.json()['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                auth=AUTH,
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_CUSTOMER_ENDPOINT, auth=AUTH)
        data = response.json()
        return data["users"]
