from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.db.models import User, Post, Comment

router = APIRouter()

@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [
        {
            "id": u.id,
            "name": u.name,
            "email": u.email
        }
        for u in users
    ]


@router.get("/users/{user_id}/posts")
def get_user_posts(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    posts = db.query(Post).filter(Post.user_id == user_id).all()
    return [
        {
            "id": p.id,
            "title": p.title,
            "body": p.body
        }
        for p in posts
    ]


@router.get("/posts/{post_id}/comments")
def get_post_comments(post_id: int, db: Session = Depends(get_db)):
    post = db.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    comments = db.query(Comment).filter(Comment.post_id == post_id).all()
    return [
        {
            "id": c.id,
            "name": c.name,
            "email": c.email,
            "body": c.body
        }
        for c in comments
    ]
