Running the Sample Project
===============================

django-pagelets includes a sample project to use as an example setup. You can run the sample project like so::

    ~$ mkvirtualenv --distribute pagelet-test
    (pagelet-test)~$ pip install -U django
    (pagelet-test)~$ git clone git://github.com/caktus/django-pagelets.git
    (pagelet-test)~$ cd django-pagelets/
    (pagelet-test)~/django-pagelets$ python setup.py develop
    (pagelet-test)~/django-pagelets$ cd sample_project/
    (pagelet-test)~/django-pagelets/sample_project$ ./manage.py syncdb
    (pagelet-test)~/django-pagelets/sample_project$ ./manage.py runserver
