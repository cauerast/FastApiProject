# FastAPI Orders API

Open-source backend solution for managing and processing **orders** across multiple business domains — from restaurants to retail or logistics, built with **FastAPI**.  
Designed for scalability, modularity, and clean architecture principles, this project provides a production-grade foundation for RESTful services.

[Documentation](#documentation) • [Installation](#installation) • [Core-Features](#core-features) • [Project-Structure](#project-structure) • [Testing](#testing) • [License](#license)

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?style=flat-square&logo=fastapi)
![License](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)
![Status](https://img.shields.io/badge/status-Active-success.svg?style=flat-square)


## Overview

**Orders API** is a backend service for managing customer orders, user authentication, and data persistence.  
It was built to serve as a reference for scalable microservices and real-world systems where reliability, performance, and maintainability are essential.

The project uses FastAPI as its core framework, with SQLAlchemy for ORM, Alembic for migrations, and Pydantic for validation.  
It is container-ready via Docker and compatible with both SQLite (for local testing) and PostgreSQL (for production).



## Core Features

- **Order Management** - endpoints for creating, updating, retrieving, and deleting orders  
- **User Authentication** - JWT-based authentication and password encryption using bcrypt  
- **Clean Architecture** - separation of routes, models, schemas, and business logic  
- **Database Migrations** - managed through Alembic  
- **Automatic Documentation** - built-in Swagger and Redoc interfaces  
- **Environment Configuration** - using `.env` files for safe variable handling  
- **Docker Support** - ready for deployment in any environment  



## Project Structure

```

📦 fastapi-orders-api
├── alembic/             # Alembic migrations
├── alembic.ini          # Alembic configuration
├── auth_routes.py       # Authentication endpoints (login, register, etc.)
├── bank.db              # SQLite database (local dev)
├── dependencies.py      # Dependency injection and utilities
├── main.py              # Application entry point
├── models.py            # SQLAlchemy ORM models
├── order_routes.py      # Endpoints for order management
├── orderSchemas/        # Pydantic schemas for order validation
├── schemas.py           # Shared Pydantic schemas
├── requirements.txt     # Project dependencies
├── .gitignore           # Git ignore configuration
└── README.md            # Project documentation

````



## Installation

### Clone the repository

```bash
git clone https://github.com/cauerast/<repository-name>.git
cd <repository-name>
````

### Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
py -m pip install fastapi uvicorn sqlalchemy alembic bcrypt==4.0.1 passlib[bcrypt] python-jose[cryptography] python-dotenv python-multipart
```

### Run the application

```bash
py -m uvicorn main:app --reload
```

## Configuration

Environment variables are defined in a `.env` file located at the root of the project.
Typical configuration values include:

```bash
DATABASE_URL=sqlite:///./bank.db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
```

## Core Design Principles

* Clean, modular code organization
* Strict type safety using Pydantic
* Layered architecture with clear domain boundaries
* Structured exception handling
* Integration-ready structure for other business domains (inventory, billing, etc.)


## Running with Docker

### Build and run the container

```bash
docker build -t fastapi-orders-api .
docker run -d -p 8000:8000 fastapi-orders-api
```

This creates a self-contained environment for local or cloud deployment.



## Testing

To run unit tests:

```bash
pytest
```

Tests are designed to validate core business logic and endpoint responses, ensuring stability through API evolution.


## License

This project is licensed under the **MIT License**.
See the `LICENSE` file for more information.


## Additional Resources

* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [Alembic Migrations Guide](https://alembic.sqlalchemy.org/en/latest/)
* [SQLAlchemy ORM](https://docs.sqlalchemy.org/)
* [Docker Documentation](https://docs.docker.com/)


*Developed and maintained by **Cauê Silva Rasteiro** — [cauerast@gmail.com](mailto:cauerast@gmail.com)*
