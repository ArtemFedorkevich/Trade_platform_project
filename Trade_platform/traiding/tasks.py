from Trade_platform.celery import app

@app.task
def hello_world():
  print('Something')
  print('Something2')