import sys

from django.conf import settings
from django.core.mail import EmailMessage, get_connection
from huey.contrib.djhuey import task

from .utils import dict_to_email, email_to_dict

TASK_CONFIG = {
    'retries': 3,
    'retry_delay': 60 * 5  # 5min
}
TASK_CONFIG.update(settings.HUEY_EMAIL_TASK_CONFIG)


@task(**TASK_CONFIG)
def send_emails(messages, backend_kwargs=None, **kwargs):
    # backward compat: handle **kwargs and missing backend_kwargs
    combined_kwargs = {}
    if backend_kwargs is not None:
        combined_kwargs.update(backend_kwargs)
    combined_kwargs.update(kwargs)

    # backward compat: catch single object or dict
    if isinstance(messages, (EmailMessage, dict)):
        messages = [messages]

    # make sure they're all dicts
    messages = [email_to_dict(m) for m in messages]

    conn = get_connection(backend=settings.HUEY_EMAIL_BACKEND, **backend_kwargs)

    try:
        conn.open()
    except Exception:
        sys.stderr.write("Cannot reach HUEY_EMAIL_BACKEND %s", settings.HUEY_EMAIL_BACKEND)
        raise

    messages_sent = 0

    for message in messages:
        try:
            sent = conn.send_messages([dict_to_email(message)])
            if sent is not None:
                messages_sent += sent

            sys.stdout.write("Successfully sent email message to %r.", message['to'])
        except Exception as e:
            # Not expecting any specific kind of exception here because it
            # could be any number of things, depending on the backend
            sys.stdout.write("Failed to send email message to %r, retrying. (%r)")

    conn.close()
    return messages_sent
