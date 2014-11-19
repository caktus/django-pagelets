#!/usr/bin/env python

import os
import sys
import optparse

from django.conf import settings
from django.core.management import call_command
try:
    from django import setup
except ImportError:
    def setup():
        pass

parser = optparse.OptionParser()
opts, args = parser.parse_args()

directory = os.path.abspath('%s' % os.path.dirname(__file__))

if not settings.configured:
    jenkins = []
    db_name = 'test_pagelets'
    if 'jenkins' in args:
        jenkins = ['django_jenkins']
        db_name = "pagelets_%s" % os.environ.get('TESTENV', db_name)

    settings.configure(
        AUTH_USER_MODEL='auth.User',
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'pagelets.db',
                'USER': '',
                'PASSWORD': '',
                'HOST': '',
                'PORT': '',
                'TEST_NAME': db_name,
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
            'django.contrib.webdesign',
            'pagelets',
            'selectable',
            'taggit',
        ] + jenkins,
        SITE_ID=1,
        ROOT_URLCONF='pagelets.tests.urls',
        MIDDLEWARE_CLASSES=(
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
        ),
        TEMPLATE_LOADERS=(
            'django.template.loaders.app_directories.Loader',
            'django.template.loaders.filesystem.Loader',
        ),
        TEMPLATE_CONTEXT_PROCESSORS=(
            "django.contrib.auth.context_processors.auth",
            "django.core.context_processors.debug",
            "django.core.context_processors.i18n",
            "django.core.context_processors.media",
            "django.core.context_processors.static",
            "django.contrib.messages.context_processors.messages",
            'django.core.context_processors.request',
        ),
        TEMPLATE_DIRS=(
            '%s/sample_project/templates' % directory,
        ),
        PASSWORD_HASHERS=['django.contrib.auth.hashers.MD5PasswordHasher'],  # Increase speed in 1.4
        PROJECT_APPS=('pagelets',),
        JENKINS_TASKS=(
            'django_jenkins.tasks.with_coverage',
            'django_jenkins.tasks.django_tests',
            'django_jenkins.tasks.run_pep8',
        ),
    )


def run_jenkins_tests():
    kwargs = {
        'pep8-exclude': 'migrations',
        'pep8-select': '',
        'pep8-ignore': '',
        'pep8-max-line-length': 80,
        'coverage-exclude': 'pagelets.migrations',
        'coverage_with_migrations': False,
        'coverage_html_report_dir': '',
        'coverage_excludes': [],
        'coverage_measure_branch': False,
        'coverage_rcfile': '',
        'output_dir': 'reports/',
    }
    call_command('jenkins', **kwargs)


from django.test.utils import get_runner


def run_django_tests():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True, failfast=False)
    failures = test_runner.run_tests(['pagelets'])
    sys.exit(failures)


def run():
    setup()
    if 'jenkins' in args:
        run_jenkins_tests()
    else:
        run_django_tests()

if __name__ == '__main__':
    run()
