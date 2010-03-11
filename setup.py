import os
from setuptools import setup, find_packages

packages = find_packages()
packages += [
    'pagelets.templates',
    'pagelets.templates.pagelets',
]
setup(
    name='django-pagelets',
    version='0.0.1',
    author='Caktus Consulting Group',
    author_email='solutions@caktusgroup.com',
    packages=find_packages(),
    install_requires = ['Django >= 1.1,==dev'],
    include_package_data = True,
    exclude_package_data={
        '': ['*.sql', '*.pyc'],
        'pagelets': ['media/*'],
    },
    url='http://code.google.com/p/django-pagelets/',
    license='LICENSE.txt',
    description='Simple, flexible app for integrating static, unstructured '
                'content in a Django site',
    long_description=open('README.txt').read(),
)
