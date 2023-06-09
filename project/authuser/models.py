from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from helpers.models import TrackingModel
import jwt
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import datetime, timedelta
from django.conf import settings


class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):

        if not username:
            raise ValueError('Username must be provided.')

        if not email:
            raise ValueError('Email must be provided.')

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is False:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is False:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, TrackingModel):

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    email = models.EmailField(
        _('email address'),
        blank=False,
        unique=True
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'),
    )

    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into the admin site.'),
    )

    email_verified = models.BooleanField(
        _('email verified'),
        default=False,
        help_text=_('Designates whether user email is verified.'),
    )

    date_joined = models.DateTimeField(
        _('date joined'),
        default=timezone.now
    )

    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def token(self):
        token = jwt.encode({
            'username': self.username,
            'email': self.email,
            'exp': datetime.utcnow() + timedelta(hours=24)}, # ! change
            settings.SECRET_KEY, algorithm='HS256')

        return token

    # set list of ids for received letters
    @property
    def received_letter_ids(self):
        return [letter.id for letter in self.received_letters.all()]

    # todo: draft letter ids