import jwt
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework import exceptions

from authuser.models import User

from django.conf import settings


class JWTAuthentication(BaseAuthentication):

    """
    JWT Authentication for DRF
    """

    def authenticate(self, request):

        auth_header = get_authorization_header(request)
        auth_data = auth_header.decode('utf-8')

        try:

            token_scheme, token = auth_data.split(" ")

            if token_scheme != "Bearer":
                raise exceptions.AuthenticationFailed(
                    "Invalid token scheme"
                )

            payload = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithm="HS256"
            )

            username = payload['username']

            user = User.objects.get(username=username)
            return (user, token)

        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("No such user")

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed(
                "Token has expired; please login again.")

        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed(
                "Invalid token, please login again.")

