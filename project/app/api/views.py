from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from letter.models import Letter
from letter.serializers import LetterSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """customize token to include username"""

    @classmethod
    def get_token(cls, user):

        token = super().get_token(user)

        token['username'] = user.username

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    """Get list of all API routes"""

    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getLetters(request):
    user = request.user
    letters = Letter.objects.filter(current_owner=user)
    serializer = LetterSerializer(letters, many=True)
    return Response(serializer.data)
