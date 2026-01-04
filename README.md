# User Data Sync Service

Backend service for asynchronous synchronization of users, posts and comments
from an external API into a PostgreSQL database.

---

##  Stack

- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy
- Celery
- Redis
- Docker & Docker Compose

---

##  Functionality

- Asynchronous data synchronization from jsonplaceholder.typicode.com
- Background processing using Celery
- Relational database structure:
  - User → Posts → Comments
- REST API for viewing stored data

---

##  Run project

Start all services:
```bash
docker-compose up -d --build
```

Database tables are created automatically on application startup.

---

##  Run background jobs

```bash
docker exec -it user-data-sync-celery_worker-1 bash
python -c "from app.jobs.sync_users_from_api import sync_users_from_api; sync_users_from_api.delay()"
python -c "from app.jobs.sync_posts_from_api import sync_posts_from_api; sync_posts_from_api.delay()"
python -c "from app.jobs.sync_comments_from_api import sync_comments_from_api; sync_comments_from_api.delay()"
exit
```

Expected result:
- Users → 10
- Posts → 100
- Comments → 500

---

##  API

Swagger UI:
```
http://localhost:8000/docs
```

Available endpoints:
- GET /users
- GET /users/{user_id}/posts
- GET /posts/{post_id}/comments

---