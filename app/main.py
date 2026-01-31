from fastapi import FastAPI, Form
from app.database import SessionLocal, engine
from app.models import Project, Base
from app.emailer import send_project_email
import os

if os.getenv("RAILWAY_ENVIRONMENT"):
    print("Running on Railway")


app = FastAPI()

@app.post("/submit-project")
def submit_project(
    plan: str = Form(...),
    genre: str = Form(...),
    service: str = Form(...),
    details: str = Form(...)
):
    db = SessionLocal()

    project = Project(
        plan=plan,
        genre=genre,
        service=service,
        details=details
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    # send_project_email(project)

    return {"status": "success"}

Base.metadata.create_all(bind=engine)
