from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
# from PIL import Image


class Letter (models.Model):
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

    '''Actual datetime when letter was created'''
    created_at = models.DateTimeField(
        default = timezone.now,
    )

    title = models.CharField(
        max_length=100,
        blank=True,
    )

    '''User-defined 'date' on letter'''
    date = models.CharField(
        max_length=2500,
        blank=True,
    )

    header = models.CharField(
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
        help_text='Regards,'
    )

    signature = models.CharField(
        max_length=2500,
        blank=True,
    )

    postscript = models.CharField(
        max_length=2500,
        blank=True,
        help_text='P.S. [message]'
    )

    status = models.CharField(
        max_length=25,
        choices=STATUS_CHOICES,
        default=DRAFT,
    )

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Letter, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('letter_detail', kwargs={'letter_id': self.id})




'''
Envelope Model

'''
class Envelope (models.Model):

    return_address = models.CharField(
        max_length=2500,
        blank=True,
    )

    address = models.CharField(
        max_length=2500,
        blank=True,
    )

    # TODO : stamps as Images (with Pillow?)
    # stamp = models.ImageField(
    #     upload_to='media/',
    #     blank=True,
    #     null=True,
    # )

    stamp = models.CharField(
        max_length=2500,
        blank=True,
    )


    def __str__(self):
        return self.address

    def save(self, *args, **kwargs):
        self.slug = slugify(self.address)
        super(Envelope, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('envelope_detail', kwargs={'envelope_id': self.id})

