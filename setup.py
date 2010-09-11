import os
from setuptools import setup, find_packages
from pagelets import __version__

classifiers = """
Topic :: Internet :: WWW/HTTP :: Dynamic Content
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules
Development Status :: 4 - Beta
Operating System :: OS Independent
"""

setup(
    name='django-pagelets',
    version=__version__,
    author='Caktus Consulting Group',
    author_email='solutions@caktusgroup.com',
    packages=find_packages(exclude=['sample_project']),
    include_package_data=True,
    url='http://http://github.com/caktus/django-pagelets',
    license='LICENSE.txt',
    description='Simple, flexible app for integrating static, unstructured '
                'content in a Django site',
    classifiers=filter(None, classifiers.split("\n")),
    long_description=open('README.rst').read(),
)
