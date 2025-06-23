import os
# gunicorn_config.py
bind = "0.0.0.0:8080"
# Get the number of CPU cores available
cpu_cores = os.cpu_count()
if cpu_cores < 1 :
    cpu_cores = 1
# Calculate the number of workers based on Gunicorn's recommendation
workers = (2 * cpu_cores) + 1 
worker_class = "uvicorn.workers.UvicornWorker"
timeout = 120
keepalive = 120
user = 'fastapiuser'
group = 'fastapiuser'

