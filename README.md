# Beauty Saloon Application

Welcome to the Beauty Saloon Application! This project is designed to manage appointments, customers, and attendants for a beauty saloon. The application is built using Python 3.12, Flask, and SQLAlchemy, and is designed to be scalable and easy to maintain.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Database Migrations](#database-migrations)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features
- Manage appointments with clients and attendants.
- Ensure no client is double-booked with the same attendant at the same time.
- Store client details (name, phone number, email).
- Store attendant details (name, unique identifier, login, password).
- RESTful API with HTTP status codes.

## Technologies
- Python 3.12
- Flask
- SQLAlchemy
- SQL Server

## Installation

### Prerequisites
- Python 3.12
- SQL Server
- Git

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/beauty-saloon.git
    cd beauty-saloon
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure your database connection in `config.py`:
    ```python
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://username:password@server/database?driver=ODBC+Driver+17+for+SQL+Server'
    ```

5. Run database migrations:
    ```bash
    flask db upgrade
    ```

6. Start the Flask application:
    ```bash
    flask run
    ```

## Usage
Once the server is running, you can interact with the API using tools like `curl`, `Postman`, or directly through your application.

### Example Request
To create a new client:
```bash
curl -X POST http://localhost:5000/clients -H "Content-Type: application/json" -d '{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "phone_number": "123-456-7890"
}'
