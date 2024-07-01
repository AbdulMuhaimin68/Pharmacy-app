# Pharmacy Management System

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Pharmacy Management System is a Flask-based web application designed to manage the operations of a pharmacy. It allows for the management of products, customers, orders, and stocks.

## Features
- User authentication and authorization
- Manage products, formulas, distributors, customers, companies, and orders
- Generate order receipts
- JWT-based authentication

## Technologies Used
- Flask
- SQLAlchemy
- Marshmallow
- MySQL
- JWT

## Installation
### Prerequisites
- Python 3.8+
- MySQL

### Steps
1. Clone the repository:
    ```bash
    git https://github.com/aziz-ullah/Pharmacy-app.git
    cd Pharmacy-app
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration
### Database Configuration
Update the database configuration in `config.py`:
```python
DB_NAME = 'pharmacy'
DB_URL = 'localhost'
DB_USER = 'root'
DB_PWD = 'your_password'
DB_PORT = 3306
JWT_SECRET_KEY = 'your_jwt_secret_key'
