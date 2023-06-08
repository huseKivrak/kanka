from rest_framework import generics
from .models import Letter, Envelope
from .serializers import LetterSerializer, EnvelopeSerializer



class ListLetters(generics.ListAPIView):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer

class ListEnvelopes(generics.ListAPIView):
    queryset = Envelope.objects.all()
    serializer_class = EnvelopeSerializer


