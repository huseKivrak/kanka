from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from helpers.models import TrackingModel


# from PIL import Image


class Letter (TrackingModel):
    DRAFT = 'draft'
    SENT = 'sent'
    DELIVERED = 'delivered'
    READ = 'read'

    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (SENT, 'Sent'),
        (DELIVERED, 'Delivered'),
        (READ, 'Read'),
    ]

    title = models.CharField(
        max_length=100,
        blank=True,
    )

    # 'Date' user field for letter
    date = models.CharField(
        max_length=2500,
        blank=True,
    )

    opener = models.CharField(
        max_length=2500,
        blank=True,
        help_text='Dear [name],'
    )

    body = models.CharField(
        max_length=2500,
        blank=True,
    )

    closer = models.CharField(
        max_length=2500,
        blank=True,
        help_text='Regards,',
        verbose_name='Complimentary close'
    )

    # TODO: allow users to upload signature image
    signature = models.CharField(
        max_length=2500,
        blank=True,
    )

    postscript = models.CharField(
        max_length=2500,
        blank=True,
        help_text='P.S. [message]'
    )

    # 'draft'(default), 'sent', 'delivered', 'read'
    status = models.CharField(
        max_length=25,
        choices=STATUS_CHOICES,
        default=DRAFT,
    )

    author = models.ForeignKey(
        User,
        related_name='authored_letters',
        on_delete=models.CASCADE
    )

    recipient = models.ForeignKey(
        User,
        related_name='received_letters',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('letter_detail', kwargs={'letter_id': self.id})

    @property
    def current_owner(self):
        if self.status == 'draft' or self.status == 'sent':
            return self.author
        elif self.status in ['delivered', 'read']:
            return self.recipient


'''
Envelope Model
'''


class Envelope (TrackingModel):

    return_address = models.CharField(
        max_length=2500,
        blank=True,
        verbose_name='Return Address',
    )

    address = models.CharField(
        max_length=2500,
        blank=True,
    )

    # TODO : stamp as ImageField (with Pillow?) or own model?
    # stamp = models.ImageField(
    #     upload_to='media/',
    #     blank=True,
    #     null=True,
    # )

    stamp = models.CharField(
        max_length=2500,
        blank=True,
    )

    letter = models.OneToOneField(
        Letter,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return reverse('envelope_detail', kwargs={'envelope_id': self.id})
