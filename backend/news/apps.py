from django.apps import AppConfig
import sys

class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    # def ready(self):
    #     # Don’t run this during commands like migrate, makemigrations, etc.
    #     if any(
    #         command in sys.argv
    #         for command in ['makemigrations', 'migrate', 'collectstatic', 'shell', 'createsuperuser', 'test']
    #     ):
    #         return

    #     from django_celery_beat.models import PeriodicTask, CrontabSchedule

    #     schedule, created = CrontabSchedule.objects.get_or_create(
    #         minute='*',
    #         hour='*',
    #         day_of_week='*',
    #         day_of_month='*',
    #         month_of_year='*',
    #     )

    #     PeriodicTask.objects.get_or_create(
    #         crontab=schedule,
    #         name='check update',
    #         task='news.tasks.check_update',
    #     )
