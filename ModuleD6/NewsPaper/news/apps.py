from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):

        from .tasks import send_mails
        from .scheduler import subscribe_scheduler

        subscribe_scheduler.add_job(
            id='send mail',
            func=send_mails,
            trigger='interval',
            # seconds=30
            days=7
        )
        subscribe_scheduler.start()



