"""
Main FastAPI application for user authentication and project management.
"""

from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session

from app import database, schemas, crud
from app.auth import create_access_token
from app.dependencies import get_current_user, require_admin
from app.database import get_session

app = FastAPI()


@app.on_event("startup")
def on_startup():
    """
    Initialize the database on application startup.
    """
    database.init_db()


@app.post("/register", status_code=201)
def register(user: schemas.UserCreate, session: Session = Depends(get_session)):
    """
    Register a new user.
    """
    return crud.create_user(user, session)


@app.post("/login", response_model=schemas.Token)
def login(form_data: schemas.UserLogin, session: Session = Depends(get_session)):
    """
    Authenticate user and return access token.
    """
    user = crud.authenticate_user(form_data.username, form_data.password, session)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(user)
    return {"access_token": token, "token_type": "bearer"}


@app.get("/projects", response_model=list[schemas.ProjectRead])
def read_projects(
    user=Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Retrieve all projects. Requires authentication.
    """
    return crud.get_projects(session)


@app.post("/projects", status_code=201)
def create_project(
    project: schemas.ProjectCreate,
    session: Session = Depends(get_session),
    admin_user=Depends(require_admin)
):
    """
    Create a new project. Admin access required.
    """
    return crud.create_project(project, session)


@app.put("/projects/{project_id}")
def update_project(
    project_id: int,
    project_data: schemas.ProjectCreate,
    session: Session = Depends(get_session),
    admin_user=Depends(require_admin)
):
    """
    Update an existing project by ID. Admin access required.
    """
    updated = crud.update_project(project_id, project_data, session)
    if not updated:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated


@app.delete("/projects/{project_id}")
def delete_project(
    project_id: int,
    session: Session = Depends(get_session),
    admin_user=Depends(require_admin)
):
    """
    Delete a project by ID. Admin access required.
    """
    deleted = crud.delete_project(project_id, session)
    if not deleted:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"detail": "Deleted successfully"}
