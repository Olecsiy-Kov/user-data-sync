import requests
from app.core.celery_app import celery_app
from app.db.session import SessionLocal
from app.db.models import Comment, Post

@celery_app.task
def sync_comments_from_api():
    response = requests.get("https://jsonplaceholder.typicode.com/comments")
    comments = response.json()

    db = SessionLocal()

    for c in comments:
        post = db.get(Post, c["postId"])
        if not post:
            continue

        if not db.get(Comment, c["id"]):
            db.add(Comment(
                id=c["id"],
                name=c["name"],
                email=c["email"],
                body=c["body"],
                post_id=post.id
            ))

    db.commit()
    db.close()
