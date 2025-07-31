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

**⚙️ Installation**

1) Clone the repository:
   git clone https://github.com/ashiq-pm/coding-sphere-fastapi.git
   cd coding-sphere-fastapi

2) Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate

3) Install dependencies:
   pip install -r requirements.txt

4) Set environment variables
   Create a .env file in the project root:
   SECRET_KEY=022ac0cbda83e3609d7001bdd5b4aef00c23486cb3ab29bda09d429683ba57c5
   DATABASE_URL=postgresql://postgres:codingsphere@localhost:5432/coding_sphere

5) Run the FastAPI server:
   uvicorn main:app --reload

**🧾 Dependencies**
fastapi  
sqlmodel  
uvicorn  
passlib  
python-jose  
psycopg2-binary  
python-dotenv  
pydantic


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

