import os
from setuptools import setup, find_packages

packages = find_packages()
packages += [
    'pagelets.templates',
    'pagelets.templates.pagelets',
]
setup(
    name='Pagelets',
    version='0.0.0',
    author='Caktus Consulting Group',
    author_email='solutions@caktusgroup.com',
    packages=find_packages(),
    include_package_data = True,
    exclude_package_data={ '': ['*.sql','*.pyc'] },
    url='http://code.google.com/p/django-pagelets/',
    license='LICENSE.txt',
    description='Simple, flexible app for integrating static, unstructured content in a Django site',
    long_description=open('README.txt').read(),
)
