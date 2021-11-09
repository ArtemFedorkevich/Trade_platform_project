from __future__ import absolute_import
import os
from celery import Celery

# этот код скопирован с manage.py
# он установиflower -A celery_django --port=5555т модуль настроек по умолчанию Django для приложения 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Trade_platform.settings')

# здесь вы меняете имя
app = Celery("Trade_platform")

# Для получения настроек Django, связываем префикс "CELERY" с настройкой celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# загрузка tasks.py в приложение django
app.autodiscover_tasks()


@app.task
def add(x, y):
    return x / y
