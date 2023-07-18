
import os
import googlemaps
from django.utils import timezone
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger(__name__)


# Google Maps API Key
API_KEY = os.getenv("GOOGLE_DISTANCE_MATRIX_API_KEY")
# Google Maps API Client
gmaps = googlemaps.Client(key=API_KEY)


class DeliveryEstimator:
    """
    Utility class for determining delivery date of a letter based on the
    distance between author and recipient zip codes.
        1. Google Distance Matrix API Call for distance
        2. Approximate delivery days
        3. Return as new datetime
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
                logger.error(
                    f"Matrix error: {matrix['status']}; {matrix['error_message']}")
                return None

            element = matrix["rows"][0]["elements"][0]
            if element["status"] != "OK":
                logger.error(
                    f"Element error: {element['status']}; {element['error_message']}")
                return None

            # Get distance
            distance_str = element["distance"]["text"]
            distance = float(distance_str.split()[0])
            return distance

        except Exception as e:
            logger.exception(e)
            return None

    def estimate_delivery_days(self, distance):
        """
        Just returns an integer between 1-5 based on distance value.

        Separated out for easy updating/replacing later.
        """

        delivery_days = [
            (50, 1),
            (300, 2),
            (1000, 3),
            (2000, 4),
        ]

        for max_distance, days in delivery_days:
            if distance <= max_distance:
                return days

        return 5

    def calculate_delivery_date(self, send_date, delivery_days):
        """
        Returns a new datetime that is the send_date + 1-5 days.
            - if that date falls on a Sunday, adds an extra day.

        As above, separated out for easy updating/replacing later.
        """
        date = send_date + timezone.timedelta(days=delivery_days)

        if date.weekday() == 6:
            date += timezone.timedelta(days=1)
            logger.debug(f"Sunday delivery; new date: {date}")

        return date

    def get_delivery_date(self, zip1, zip2, send_date):
        """
        Facade method for getting delivery date. Also
        """
        try:
            distance = self.get_distance_between_zip_codes(zip1, zip2)
            logger.debug(
                f"Distance between {zip1} and {zip2} is {distance} miles")

            delivery_days = self.estimate_delivery_days(distance)
            logger.debug(f"Delivery days: {delivery_days}")

            delivery_date = self.calculate_delivery_date(
                send_date, delivery_days)
            logger.debug(f"Delivery date: {delivery_date}")

            return delivery_date

        except Exception as e:
            logger.exception(e)
            return None
