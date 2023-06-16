
from dotenv import load_dotenv
load_dotenv()
from os import getenv

ZIPCODE_API_KEY = getenv("ZIPCODE_API_KEY")

import requests

import math

class DistanceService:

    @staticmethod
    def calculate_distance(letter):
        user_zip = letter.author.zipcode
        recipient_zip = letter.recipient.zipcode

        distance = DistanceService.get_distance(user_zip, recipient_zip)

        # delivery_time: every 500 miles is 1 day
        delivery_time = math.ceil(distance / 500)

        # maximum of 5 days
        delivery_time = min(delivery_time, 5)

        letter.delivery_time = delivery_time
        letter.save()



    @staticmethod
    def get_distance(zip1, zip2):
        api_key = ZIPCODE_API_KEY
        url = f"https://www.zipcodeapi.com/rest/{api_key}/distance.json/{zip1}/{zip2}/mile"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            distance = data['distance']
            return distance
        else:
            raise Exception("ZipcodeAPI error", response.status_code)
