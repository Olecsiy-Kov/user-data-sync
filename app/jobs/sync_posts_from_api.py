import requests
from app.core.celery_app import celery_app
from app.db.session import SessionLocal
from app.db.models import Post, User

@celery_app.task
def sync_posts_from_api():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = response.json()

    db = SessionLocal()

    for p in posts:
        user = db.get(User, p["userId"])
        if not user:
            continue

        if not db.get(Post, p["id"]):
            db.add(Post(
                id=p["id"],
                title=p["title"],
                body=p["body"],
                user_id=user.id
            ))

    db.commit()
    db.close()
