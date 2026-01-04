import requests
from app.core.celery_app import celery_app
from app.db.session import SessionLocal
from app.db.models import User

@celery_app.task
def sync_users_from_api():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()

    db = SessionLocal()

    for u in users:
        if not db.get(User, u["id"]):
            db.add(User(
                id=u["id"],
                name=u["name"],
                email=u["email"]
            ))

    db.commit()
    db.close()
