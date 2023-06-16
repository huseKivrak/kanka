from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status

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


class LetterList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        authored_letters = Letter.objects.filter(
            author=user,
            status=Letter.DRAFT
        )
        received_letters = Letter.objects.filter(
            recipient=user,
            status__in=[Letter.DELIVERED, Letter.READ]
        )
        letters = authored_letters.union(received_letters)

        serializer = LetterSerializer(letters, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        serializer = LetterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(author=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LetterDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Letter.objects.get(id=pk, author=user)
        except Letter.DoesNotExist:
            return None

    def get(self, request, pk):
        letter = self.get_object(pk, request.user)
        if letter is None:
            return Response({'message': 'Letter does not exist or no view permission'}, status=status.HTTP_404_NOT_FOUND)

        serializer = LetterSerializer(letter)
        return Response(serializer.data)

    def put(self, request, pk):
        letter = self.get_object(pk, request.user)
        if letter is None:
            return Response({'message': 'Letter does not exist or no update permission'}, status=status.HTTP_404_NOT_FOUND)

        serializer = LetterSerializer(letter, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        letter = self.get_object(pk, request.user)
        if letter is None:
            return Response({'message': 'Letter does not exist or no delete permission'}, status=status.HTTP_404_NOT_FOUND)

        letter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
