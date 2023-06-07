from rest_framework import serializers
from app.models import Letter, Envelope

class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = '__all__'

class EnvelopeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envelope
        fields = '__all__'

