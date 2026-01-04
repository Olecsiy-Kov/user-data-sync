from celery import Celery

celery_app = Celery(
    "user_data_sync",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/1",
    include=[
        "app.jobs.sync_users_from_api",
        "app.jobs.sync_posts_from_api",
        "app.jobs.sync_comments_from_api",
    ],
)

