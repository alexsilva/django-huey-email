==========================================================
django-huey-email - A Huey-backed Django Email Backend
==========================================================


A `Django`_ email backend that uses a `Huey`_ queue for out-of-band sending
of the messages. Inspired by the project `django-celery-email`_.

.. _`Huey`: https://huey.readthedocs.io/en/latest/index.html
.. _`Huey docs`: https://huey.readthedocs.io/en/latest/index.html
.. _`Django`: https://www.djangoproject.com/
.. _`django-celery-email`: https://github.com/pmclanahan/django-celery-email
.. _`TaskResultWrapper`: https://huey.readthedocs.io/en/latest/api.html?highlight=TaskResultWrapper#TaskResultWrapper

.. warning::

	This version requires the following versions:

	* Python >= 3.0
	* Django 2.0.8
	* Huey += 1.10.2

Using django-huey-email
=========================

To enable ``django-huey-email`` for your project you need to add ``djhuey_email`` to
``INSTALLED_APPS``::

    INSTALLED_APPS += ("djhuey_email",)

You must then set ``django-huey-email`` as your ``EMAIL_BACKEND``::

    EMAIL_BACKEND = 'djhuey_email.backends.HueyEmailBackend'

By default ``django-huey-email`` will use Django's builtin ``SMTP`` email backend
for the actual sending of the mail. If you'd like to use another backend, you
may set it in ``HUEY_EMAIL_BACKEND`` just like you would normally have set
``EMAIL_BACKEND`` before you were using Huey. In fact, the normal installation
procedure will most likely be to get your email working using only Django, then
change ``EMAIL_BACKEND`` to ``HUEY_EMAIL_BACKEND``, and then add the new
``EMAIL_BACKEND`` setting from above.

Mass email are sent in chunks of size ``HUEY_EMAIL_CHUNK_SIZE`` (defaults to 10).

There are some default settings. Unless you specify otherwise, the equivalent of the
following settings will apply::

    HUEY_EMAIL_TASK_CONFIG = {
        'retries': 3,
        'retry_delay': 60 * 5  # 5min
    }

After this setup is complete, and you have a working Huey install, sending
email will work exactly like it did before, except that the sending will be
handled by your Huey workers::

    from django.core import mail

    emails = (
        ('Hey Man', "I'm The Dude! So that's what you call me.", 'dude@aol.com', ['mr@lebowski.com']),
        ('Dammit Walter', "Let's go bowlin'.", 'dude@aol.com', ['wsobchak@vfw.org']),
    )
    results = mail.send_mass_mail(emails)

``results`` will be a list of huey `TaskResultWrapper`_ objects that you may ignore, or use to check the
status of the email delivery task, or even wait for it to complete if want.
You should also set ``HUEY_EMAIL_CHUNK_SIZE = 1`` in settings if you are concerned about task status
and results.

See the `Huey docs`_ for more info.


``len(results)`` will be the number of emails you attempted to send divided by HUEY_EMAIL_CHUNK_SIZE, and is in no way a reflection on the success or failure
of their delivery.


Changelog
=========

