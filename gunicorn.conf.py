bind = "127.0.0.1:8000"                   # Don't use port 80 becaue nginx occupied it already. 
errorlog = '/Users/agupta/Desktop/DJANGO_REALESTATE/django-realestate/logs/gunicorn-error.log'  # Make sure you have the log folder create
accesslog = '/Users/agupta/Desktop/DJANGO_REALESTATE/django-realestate/logs/gunicorn-access.log'
loglevel = 'debug'
workers = 1     # the number of recommended workers is '2 * number of CPUs + 1' 