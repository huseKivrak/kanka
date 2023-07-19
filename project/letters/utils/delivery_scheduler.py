from apscheduler.schedulers.background import BackgroundScheduler
from letters.models import Letter
from django.utils import timezone
import logging

scheduler = BackgroundScheduler()
logger = logging.getLogger(__name__)

def deliver_letters():
    letters = Letter.letters.sents()
    for letter in letters:
        if letter.delivery_date <= timezone.now():
            letter.deliver()
            logger.info(f"Delivered letter {letter.pk} to {letter.recipient}")



def start():
    scheduler.add_job(
        deliver_letters,
        'interval',
        hours=1,
        id='deliver_letters',
        replace_existing=True,
    )

    scheduler.start()
