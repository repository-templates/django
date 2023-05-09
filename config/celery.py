import os
from celery import Celery
from celery.signals import setup_logging
from celery.schedules import crontab
from celery.utils.log import get_task_logger
from kombu import Exchange, Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

logger = get_task_logger(__name__)

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Configure periodic tasks
app.conf.beat_schedule = {
    #'schedule_emails': {
    #    'task': 'example.tasks.schedule_emails',
    #    'schedule': crontab(minute='*/10'),
    #},
}


@setup_logging.connect
def config_loggers(*args, **kwargs):
    from logging.config import dictConfig
    from django.conf import settings
    dictConfig(settings.LOGGING)


@app.task(bind=True)
def debug_task(self):
    logger.info('Debug task is running!')
    print(f'Request: {self.request!r}')
