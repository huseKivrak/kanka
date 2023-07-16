from django.forms import ModelForm
from .models import Letter

class LetterForm (ModelForm):
    class Meta:
        model = Letter
        fields = ["title", "body"]