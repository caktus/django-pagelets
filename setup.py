from setuptools import setup, find_packages

setup(
    name='django-pagelets',
    version=__import__('pagelets').__version__,
    author='Caktus Consulting Group',
    author_email='solutions@caktusgroup.com',
    packages=find_packages(exclude=['sample_project']),
    include_package_data=True,
    url='http://github.com/caktus/django-pagelets/',
    license='BSD',
    description='Simple, flexible app for integrating static, unstructured '
                'content in a Django site',
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
    ],
    long_description=open('README.rst').read(),
    zip_safe=False,  # because we're including media that Django needs
    install_requires=[
        "django-selectable>=0.9.0",
        "django-taggit>=0.12.1",
    ],
)
