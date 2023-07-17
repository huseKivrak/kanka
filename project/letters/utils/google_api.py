
import os
import googlemaps
from django.utils import timezone
from dotenv import load_dotenv

load_dotenv()

# Google Maps API Key
API_KEY = os.getenv("GOOGLE_DISTANCE_MATRIX_API_KEY")
# Google Maps API Client
gmaps = googlemaps.Client(key=API_KEY)

class DeliveryEstimator:
    """
    Utility class for estimating delivery date of a letter based on the
    distance between author and recipient zip codes.
    """

    def __init__(self, gmaps_client=gmaps):
        self.gmaps = gmaps_client

    def get_distance_between_zip_codes(self, zip1, zip2):
        """
        Uses googlemaps' Python Client to get the distance between two zip codes.
        """

        try:
            # Request distance matrix
            matrix = self.gmaps.distance_matrix(
                origins=zip1,
                destinations=zip2,
                units="imperial",
            )

            if matrix["status"] != "OK":
                print(
                    f"Error with distance matrix request: {matrix['error_message']}")
                return None

            element = matrix["rows"][0]["elements"][0]
            if element["status"] != "OK":
                print(f"Error calculating distance: {element['status']}")
                return None

            # Get distance
            distance_str = element["distance"]["text"]
            distance = float(distance_str.split()[0])
            return distance

        except Exception as e:
            print(e)
            return None

    def estimate_delivery_days(self, distance):
        """
        Estimates delivery time based on distance (miles).
        """
        if distance <= 50:
            return 1
        elif distance <= 300:
            return 2
        elif distance <= 1000:
            return 3
        elif distance <= 2000:
            return 4
        else:
            return 5

    def calculate_delivery_date(self, send_date, delivery_days):
        """
        Calculates delivery date based on send date and delivery days.
        """
        return send_date + timezone.timedelta(days=delivery_days)

    def get_delivery_date(self, zip1, zip2, send_date):
        try:
            distance = self.get_distance_between_zip_codes(zip1, zip2)
            delivery_days = self.estimate_delivery_days(distance)
            delivery_date = self.calculate_delivery_date(send_date, delivery_days)

            # Add 1 day if delivery date falls on a Sunday
            if delivery_date.weekday() == 6:
                delivery_date += timezone.timedelta(days=1)

            return delivery_date

        except Exception as e:
            print(f"failed to get delivery date: {e}")
            return None


