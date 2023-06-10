from rest_framework import serializers
from .models import Letter, Envelope

class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = '__all__'

class EnvelopeSerializer(serializers.Serializer):
    class Meta:
        model = Envelope
        fields = '__all__'
        read_only_fields = [
            'id',
            'created_at',
        ]
