from django.apps import AppConfig
from utils import delivery_scheduler

class LettersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'letters'

    def ready(self):
        print("starting delivery scheduler")
        delivery_scheduler.start()