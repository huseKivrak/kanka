from rest_framework import serializers
from .models import Letter, Envelope

class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = '__all__'
