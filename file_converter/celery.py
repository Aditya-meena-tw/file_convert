# from celery import Celery
# import os

# # Set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'file_converter.settings')

# '''For local celery worker '''
# import os
# from celery import Celery

# # setting the Django settings module.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'file_converter.settings')
# app = Celery('file_converter')
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Looks up for task modules in Django applications and loads them
# app.autodiscover_tasks()

'''For Docker celery worker '''

import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'file_converter.settings')

app = Celery('file_converter')

# Update the broker URL to use Redis container's hostname or IP address
app.conf.broker_url = 'redis://redis:6379/0'
# or app.conf.broker_url = 'redis://<Redis_Container_IP>:6379/0'

# Set other Celery configurations if needed
# app.conf.<config_name> = <config_value>

# Looks up for task modules in Django applications and loads them
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')