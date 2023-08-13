
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
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
        user = self.model(email=email, username=username,
                          zip_code=zip_code)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractUser):
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

    friends = models.ManyToManyField(
        'self',
        symmetrical=True,
        through='FriendRequest',
        through_fields=('from_user', 'to_user'),
    )

    objects = UserProfileManager()

    REQUIRED_FIELDS = ['email', 'zip_code']

    def __str__(self):
        return self.username


class FriendRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    from_user = models.ForeignKey(
        CustomUser, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        CustomUser, related_name='to_user', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=8, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f'{self.from_user} - {self.to_user}'

    class Meta:
        unique_together = ('from_user', 'to_user')
        index_together = ('from_user', 'to_user')

    def accept(self):
        """Accept friend request"""
        self.status = 'accepted'
        self.remove_request()

        self.from_user.friends.add(self.to_user)
        self.to_user.friends.add(self.from_user)

        self.delete()

    def reject(self):
        """Reject friend request"""
        self.status = 'rejected'
        self.save()
        self.remove_request()

    def remove_request(self):
        """Remove friend request"""
        super(FriendRequest, self).delete()

    @classmethod
    def get_requests(cls, user):
        """Return all pending friend requests for a user"""
        return cls.objects.filter(to_user=user, status='pending')
