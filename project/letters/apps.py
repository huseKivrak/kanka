from django.apps import AppConfig


class LettersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'letters'

    def ready(self):
        from letters.utils import delivery_scheduler
        print("starting delivery scheduler")
        delivery_scheduler.start()
