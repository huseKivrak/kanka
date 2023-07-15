from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            "email",
            "username",
            "zip_code",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            "email",
            "username",
            "zip_code",
        )
