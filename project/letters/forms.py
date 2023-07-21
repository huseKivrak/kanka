from django.forms import ModelForm
from .models import Letter
from django import forms

class LetterForm (ModelForm):
    class Meta:
        model = Letter
        fields = ["title", "body", "recipient"]

        # check that recipient is a valid user:
        def clean_recipient(self):
            recipient = self.cleaned_data["recipient"]
            if not recipient.is_active:
                raise forms.ValidationError("No such user")
            return recipient