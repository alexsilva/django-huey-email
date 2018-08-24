from django import apps


class HueyEmailAppConfig(apps.AppConfig):
    TASK_CONFIG = {}
    BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    CHUNK_SIZE = 10
    MESSAGE_EXTRA_ATTRIBUTES = None

    name = 'djhuey_email'

    verbose_name = 'HUEY TASK'
