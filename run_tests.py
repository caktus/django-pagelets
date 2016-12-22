#!/usr/bin/env python

import os
import sys
import optparse

from django.conf import settings
from django import setup
from django.test.utils import get_runner

parser = optparse.OptionParser()
opts, args = parser.parse_args()

directory = os.path.abspath('%s' % os.path.dirname(__file__))

if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'pagelets.db',
                'USER': '',
                'PASSWORD': '',
                'HOST': '',
                'PORT': '',
            }
        },
        INSTALLED_APPS=[
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'pagelets',
            'selectable',
            'taggit',
        ],
        ROOT_URLCONF='pagelets.tests.urls',
        MIDDLEWARE_CLASSES=(
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
        ),
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': ['%s/sample_project/templates' % directory],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        "django.contrib.auth.context_processors.auth",
                        "django.template.context_processors.debug",
                        "django.template.context_processors.i18n",
                        "django.template.context_processors.media",
                        "django.template.context_processors.static",
                        "django.contrib.messages.context_processors.messages",
                        'django.template.context_processors.request',
                    ]
                },
            },
        ],
        STATIC_URL='/static/',
    )


def run_django_tests():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True, failfast=False)
    failures = test_runner.run_tests(['pagelets'])
    sys.exit(failures)


def run():
    setup()
    run_django_tests()


if __name__ == '__main__':
    run()
