# FastAPI, React, SQLite CRUD Template
This repository is designed as a template for anyone who wishes to build full-stack applications using FastAPI for the backend, React for the frontend, SQLite for the database, and Docker for containerization. It's a versatile, lightweight, and powerful stack that I've used for both personal projects and internal company applications.

## Why I Chose This Stack
- FastAPI: Fast, modern, and asynchronous framework for building APIs with Python.
- React: One of the most popular JavaScript libraries for building user interfaces.
- SQLite: A simple, lightweight database engine that's perfect for small to medium-sized applications.
- Tabler: A free and open-source web application UI kit based on Bootstrap 5, with hundreds of responsive components and multiple layouts.
- Docker: Easy setup and deployment across different environments, ensuring that "it works on my machine" for everyone.

## Overview
This diagram illustrates the project architecture:
![Project Architecture](https://github.com/Ballal65/FastAPI-SQLlite-React-Tabler--CRUD-Template-Without-authentication/blob/main/Docker%20Overview.png)

# Backend
## Folder Structure
```
|- backend
|--- app
|------ __init__.py
|------ database.py   # Creating SQLite engine, Base, SessionLocal
|------ main.py       # FastAPI application entry point
|------ models.py     # SQLAlchemy models
|--- routers
|------ __init__.py
|------ vendors.py    # CRUD router for managing vendors
|--- data
|------ sql_app.db    # SQLite database file
|--- dockerfile       # Dockerfile for containerizing the FastAPI app
|--- requirements.txt # Python dependencies for the project
```
## Backend Important files
- database.py: Contains the configuration for the SQLite database and SQLAlchemy engine. It also defines SessionLocal for database session management and Base for model definitions.

- main.py: The main entry point for the FastAPI app, where the API routes are defined and FastAPI is initialized.

- models.py: Defines the database models using SQLAlchemy, which are the structure of the tables in the SQLite database.

- vendors.py: Contains CRUD operations (Create, Read, Update, Delete) for the Vendor resource using FastAPI and SQLAlchemy. Pydantic models are used for input validation.

- sql_app.db: The SQLite database file where all data for the project is stored.

- dockerfile: Defines how to containerize the FastAPI application using Docker.

![Backend Docs](https://github.com/Ballal65/FastAPI-SQLlite-React-Tabler--CRUD-Template-Without-authentication/blob/main/Backend%20Docs.png)

##Frontend
![Frontend Screenshot](https://github.com/Ballal65/FastAPI-SQLlite-React-Tabler--CRUD-Template-Without-authentication/blob/main/Frontend%20Screenshot.png)
