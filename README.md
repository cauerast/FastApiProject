# 🚀 FastAPI App - Orders API

> Modern, high-performance, and scalable API built with **FastAPI**, following clean architecture and best coding practices.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?style=flat-square&logo=fastapi)
![License](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)
![Status](https://img.shields.io/badge/status-Active-success.svg?style=flat-square)



## 📘 About the Project

This project was developed to build a robust, modular, and scalable RESTful API using the FastAPI framework.  
The application follows Clean Architecture principles, uses static typing with Pydantic, and includes automatic API documentation with Swagger and Redoc.

The main goal is to provide a solid foundation for developing modern, secure, and high-performance services — ideal for systems that demand both speed and maintainability.



## 🧠 Core Technologies

- **FastAPI** - modern and fast Python web framework for APIs  
- **Pydantic** - data validation and type enforcement  
- **Uvicorn** - high-performance ASGI server  
- **SQLAlchemy** - ORM for database management  
- **SQLite / PostgreSQL** - multi-database support  
- **Docker** - simplified containerization and deployment  
- **Git & GitHub Actions** - version control and CI/CD automation  



## ⚙️ Project Structure

```

📦 fastapi-app
├── alembic/           # Alembic migrations
├── alembic.ini        # Alembic configuration
├── auth_routes.py     # Authentication routes (login, register, etc.)
├── bank.db            # SQLite database file
├── dependencies.py    # Dependency injection and utilities
├── main.py            # Application entry point
├── models.py          # SQLAlchemy ORM models
├── order_routes.py    # Endpoints for order management
├── orderSchemas/      # Pydantic schemas for order validation
├── schemas.py         # General data schemas
├── requirements.txt   # Project dependencies
├── .gitignore         # Git ignore rules
└── README.md          # Project documentation

````



## Installation & Execution

### 1️⃣ Clone the repository

```bash
git clone https://github.com/cauerast/<repository-name>.git
cd <repository-name>
````

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies

```bash
py -m pip install fastapi uvicorn sqlalchemy alembic bcrypt=4.0.1 passlib[bcrypt] python-jose[cryptography] python-dotenv python-multipart 
```

### 4️⃣ Run the application

```bash
py -m uvicorn app.main:app --reload
```



## 🧱 Implemented Best Practices

* Modular and scalable architecture
* Data validation using **Pydantic**
* Strong static typing for safety and readability
* Structured logging and exception handling



## 🐳 Running with Docker

### Build and run

```bash
docker build -t fastapi-app .
docker run -d -p 8000:8000 fastapi-app
```



## 🧠 Author

**Cauê Silva Rasteiro** <br>
📧 [cauerast@gmail.com](mailto:cauerast@gmail.com) <br>
🔗 [github.com/cauerast](https://github.com/cauerast) | [linkedin.com/in/cauerast](https://www.linkedin.com/in/cauerast/)



## 📜 License

This project is licensed under the **MIT License**.
