"""
CRUD operations for User and Project models.
"""

from sqlmodel import Session, select

from app.models import User, Project
from app.auth import hash_password, verify_password


def create_user(user_data, session: Session):
    """
    Create a new user with hashed password.

    :param user_data: Pydantic model containing username, password, and role
    :param session: SQLModel database session
    :return: Created User object
    """
    hashed_pw = hash_password(user_data.password)
    db_user = User(
        username=user_data.username,
        hashed_password=hashed_pw,
        role=user_data.role
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def authenticate_user(username: str, password: str, session: Session):
    """
    Authenticate user by verifying username and password.

    :param username: Username string
    :param password: Plain password string
    :param session: SQLModel database session
    :return: User object if valid, else None
    """
    user = session.exec(select(User).where(User.username == username)).first()
    if user and verify_password(password, user.hashed_password):
        return user
    return None


def create_project(project_data, session: Session):
    """
    Create a new project.

    :param project_data: Pydantic model containing project fields
    :param session: SQLModel database session
    :return: Created Project object
    """
    project = Project(**project_data.dict())
    session.add(project)
    session.commit()
    session.refresh(project)
    return project


def get_projects(session: Session):
    """
    Retrieve all projects.

    :param session: SQLModel database session
    :return: List of all Project objects
    """
    return session.exec(select(Project)).all()


def update_project(project_id, project_data, session: Session):
    """
    Update a project by ID.

    :param project_id: ID of the project to update
    :param project_data: Pydantic model with updated data
    :param session: SQLModel database session
    :return: Updated Project object or None if not found
    """
    project = session.get(Project, project_id)
    if not project:
        return None
    for key, value in project_data.dict().items():
        setattr(project, key, value)
    session.commit()
    return project


def delete_project(project_id, session: Session):
    """
    Delete a project by ID.

    :param project_id: ID of the project to delete
    :param session: SQLModel database session
    :return: Deleted Project object or None if not found
    """
    project = session.get(Project, project_id)
    if project:
        session.delete(project)
        session.commit()
    return project
