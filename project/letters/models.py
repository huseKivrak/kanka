from django.db import models
from django.utils import timezone
from accounts.models import CustomUser
from core.utils import TrackingModel

# Create your models here.
class LetterQuerySet(models.QuerySet):
    def drafts(self):
        return self.filter(status='draft')

    def sents(self):
        return self.filter(status='sent')

    def delivereds(self):
        return self.filter(status='delivered')

    def reads(self):
        return self.filter(status='read')


class Letter(TrackingModel):

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('delivered', 'Delivered'),
        ('read', 'Read'),
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft',
    )

    sent_date = models.DateTimeField(
        null=True,
        blank=True,
    )

    delivery_date = models.DateTimeField(
        # Calculated after letter is sent
        null=True,
        blank=True,
    )

    title = models.CharField(
        max_length=100,
    )

    body = models.TextField(
    )

    author = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        related_name='authored_letters',
    )

    recipient = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='received_letters',
    )

    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=True,
        related_name='owned_letters',
        default=author,
    )

    def send(self):
        self.status = 'sent'
        self.sent_date = timezone.now()
        # TODO: update with ZipCodeAPI value
        self.delivery_date = self.sent_date + timezone.timedelta(days=1)
        self.save()

    def deliver(self):
        '''Called by delivery_scheduler'''
        self.status = 'delivered'
        self.owner = self.recipient
        self.save()

    def mark_as_read(self):
        self.status = 'read'
        self.save()

    def is_owned_by(self, user):
        return self.owner == user

    letters = LetterQuerySet.as_manager()

    def __str__(self):
        return self.title