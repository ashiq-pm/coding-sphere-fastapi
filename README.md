# 🛠️ FastAPI Project Management API

A secure and modular backend API built with **FastAPI**, **SQLModel**, and **PostgreSQL**, featuring JWT authentication and Role-Based Access Control (RBAC) for managing users and projects efficiently.

---

## 🚀 Features

- 🔐 **JWT Authentication** for secure access.
- 🧑‍💼 **Role-Based Access Control (RBAC)** — admin and user roles.
- 📁 **Project CRUD** functionality.
- 🗃️ **SQLModel ORM** with PostgreSQL database.
- ♻️ Clean and scalable project structure with dependency injection.
- 🌐 Ready to deploy on any cloud platform.

---

## 🧩 Tech Stack

- **FastAPI** – Modern, fast (high-performance) web framework for APIs
- **SQLModel** – ORM built on SQLAlchemy and Pydantic
- **PostgreSQL** – Production-ready relational database
- **OAuth2** – Authentication flow using JWT tokens
- **Pydantic** – Data validation

---

<pre lang="text"> ## 📁 Project Structure ```text project/ ├── app/ │ ├── __init__.py # Makes this a Python package │ ├── auth.py # JWT token & password utilities │ ├── config.py # Environment variables setup │ ├── crud.py # Database logic for user/project │ ├── database.py # Database connection & session │ ├── dependencies.py # Auth dependencies │ ├── models.py # SQLModel DB models │ └── schemas.py # Pydantic schemas for API validation ├── main.py # Main FastAPI application ├── .env # Environment variables ├── requirements.txt # Project dependencies └── README.md # Documentation ``` </pre>


---

## 📌 API Endpoints

### 🔐 Authentication

- `POST /register` — Register a new user (`admin` or `user`)
- `POST /login` — Get JWT access token

### 📁 Project Management

- `POST /projects/` — Create a new project (Admin only)
- `GET /projects/` — Retrieve list of all projects (Authenticated users)
- `GET /projects/{project_id}` — Get details of a specific project
- `PUT /projects/{project_id}` — Update project by ID (Admin only)
- `DELETE /projects/{project_id}` — Delete project by ID (Admin only)

---

"# coding-sphere-fastapi" 
"# coding-sphere-fastapi" 
