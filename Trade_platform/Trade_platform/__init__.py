from __future__ import unicode_literals

# Это позволит убедиться, что приложение всегда импортируется, когда запускается Django
from Trade_platform.celery import app as celery_app

__all__ = ('celery_app',)
