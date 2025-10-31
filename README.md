# 🚀 FastAPI Application

> Modern, high-performance, and scalable API built with **FastAPI**, following clean architecture and best coding practices.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?style=flat-square&logo=fastapi)
![License](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)
![Status](https://img.shields.io/badge/status-Active-success.svg?style=flat-square)

---

## 📘 About the Project

This project was developed to **build a robust, modular, and scalable RESTful API** using the **FastAPI** framework.  
The application follows **Clean Architecture principles**, uses **static typing with Pydantic**, and includes **automatic API documentation with Swagger and Redoc**.

The main goal is to provide a solid foundation for developing modern, secure, and high-performance services — ideal for systems that demand both speed and maintainability.

---

## 🧠 Core Technologies

- **FastAPI** — modern and fast Python web framework for APIs  
- **Pydantic** — data validation and type enforcement  
- **Uvicorn** — high-performance ASGI server  
- **SQLAlchemy** — ORM for database management  
- **SQLite / PostgreSQL** — multi-database support  
- **Docker** — simplified containerization and deployment  
- **Git & GitHub Actions** — version control and CI/CD automation  

---

## ⚙️ Project Structure

```

📦 fastapi-app
├── 📁 app
│   ├── main.py                # Application entry point
│   ├── core/                  # Core settings (env, security, etc.)
│   ├── models/                # Database models and entities
│   ├── schemas/               # Pydantic data validation schemas
│   ├── routers/               # API routes and endpoints
│   ├── services/              # Business logic
│   └── utils/                 # Helper functions
├── requirements.txt
├── Dockerfile
├── README.md
└── .env.example

````

---

## 🧩 Installation & Execution

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
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
uvicorn app.main:app --reload
```

Access the interactive API documentation:
➡️ **Swagger:** [http://localhost:8000/docs](http://localhost:8000/docs)
➡️ **Redoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🧱 Implemented Best Practices

* Modular and scalable architecture
* Data validation using **Pydantic**
* Strong static typing for safety and readability
* Automatic API documentation via **OpenAPI**
* Well-structured route management with **routers**
* Secure configuration management using **.env**
* Structured logging and exception handling

---

## 🧪 Testing

To run automated tests:

```bash
pytest
```

---

## 🐳 Running with Docker

### Build and run

```bash
docker build -t fastapi-app .
docker run -d -p 8000:8000 fastapi-app
```

---

## 🧠 Author

**Cauê Silva Rasteiro**
Software Developer | Frontend & Backend | Automation & AI
📧 [cauerast@gmail.com](mailto:cauerast@gmail.com)
🔗 [github.com/cauerast](https://github.com/cauerast) | [linkedin.com/in/cauerast](https://www.linkedin.com/in/cauerast/)

---

## 📜 License

This project is licensed under the **MIT License**.
