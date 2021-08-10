from celery import Celery
import os

os.environ.setdefault('CELERY_CONFIG_MODULE', 'celery_config')
app = Celery('tasks', broker='amqp://root:admin1234@localhost:5672/')
app.config_from_envvar('CELERY_CONFIG_MODULE')

@app.task
def add(x, y):
    return x + y



@app.task
def add(x, y):
    return x + y

@app.task
def tsum(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args[0])