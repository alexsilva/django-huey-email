from django import apps
from django.conf import settings


class HueyEmailAppConfig(apps.AppConfig):

    HUEY_EMAIL_TASK_CONFIG = getattr(settings, 'HUEY_EMAIL_TASK_CONFIG', {})
    HUEY_EMAIL_BACKEND = getattr(settings, 'HUEY_EMAIL_BACKEND',
                                 'django.core.mail.backends.smtp.EmailBackend')
    HUEY_EMAIL_MESSAGE_EXTRA_ATTRIBUTES = getattr(settings, 'HUEY_EMAIL_MESSAGE_EXTRA_ATTRIBUTES', None)
    HUEY_EMAIL_CHUNK_SIZE = getattr(settings, 'HUEY_EMAIL_CHUNK_SIZE', 1024)

    name = 'djhuey_email'

    verbose_name = 'HUEY TASK'
