
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin
from django.core.validators import RegexValidator
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, username, zip_code, password=None):
        if not email:
            raise ValueError('Users must have an email')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, zip_code=zip_code)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, zip_code, password):
        user = self.create_user(email, username, zip_code, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    username = models.CharField(
        max_length=50,
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    zip_code = models.CharField(
        max_length=5,
        validators=[RegexValidator(
            regex='^[0-9]{5}$',
            message='Zip code must be exactly 5 digits',
            code='invalid_zip_code'
        )]
    )

    objects = UserProfileManager()

    REQUIRED_FIELDS = ['email', 'zip_code']

    def __str__(self):
        return self.username

