from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication
from serializers import LetterSerializer, EnvelopeSerializer
from models import Letter, Envelope
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated


class LetterList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer


class EnvelopeList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Envelope.objects.all()
    serializer_class = EnvelopeSerializer
