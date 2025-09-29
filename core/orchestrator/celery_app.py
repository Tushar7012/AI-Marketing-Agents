from celery import Celery
import os

redis_host = os.getenv('REDIS_HOST', 'localhost')

celery_app = Celery(
    "tasks",
    broker=f"redis://{redis_host}:6379/0",
    backend=f"redis://{redis_host}:6379/0",
    include=["agents.tasks"] 
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)