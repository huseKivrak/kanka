from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from core.utils import TrackingModel

from letters.utils.google_api import DeliveryEstimator

User = get_user_model()

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
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='authored_letters',
    )

    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='received_letters',
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='owned_letters',
        default=None,
    )

    letters = LetterQuerySet.as_manager()


    def send(self):
        """
        Use Google API to estimate delivery date and save it to the letter
        """

        self.status = 'sent'
        self.sent_date = timezone.now()

        author_zip_code = self.author.zip_code
        recipient_zip_code = self.recipient.zip_code

        estimator = DeliveryEstimator()
        delivery_date = estimator.get_delivery_date(
            author_zip_code, recipient_zip_code, self.sent_date)

        self.delivery_date = delivery_date
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

    def save(self, *args, **kwargs):
        if not self.owner_id:
            if self.status == 'draft':
                self.owner_id = self.author_id
            else:
                self.owner_id = self.recipient_id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


def mailbox_count_for(user):
    """
    returns number of unread letters for a given user
    """
    return Letter.letters.delivereds().filter(owner=user).count()
