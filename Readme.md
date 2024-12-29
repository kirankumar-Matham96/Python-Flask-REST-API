# Python Flask Rest API

This repository contains a Flask API application connected to a PostgreSQL database, dockerized using Docker Compose. It provides CRUD operations for managing user data.

---

## Features

- Create, Read, Update, and Delete (CRUD) operations for user management.
- PostgreSQL database for persistent storage.
- Dockerized application for easy deployment.
- Environment variable support for database configuration.
- CORS enabled for cross-origin requests.

---

## Prerequisites

Ensure the following software is installed:

1. [Docker](https://docs.docker.com/get-docker/)
2. [Docker Compose](https://docs.docker.com/compose/install/)

---

## Project Structure

```
.
├── backend
│   ├── app.py
│   ├── requirements.txt
│   └── flask.dockerfile
├── docker-compose.yml
└── README.md
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone <repository-url>
cd <repository-folder>
```

### 2. Start the application

```
docker-compose up --build
```

This command builds and starts the Flask API and PostgreSQL database containers.

### 3. Verify running services

```
docker ps
```

Ensure both `flaskapp` and `db` containers are running.

---

## API Endpoints

### Base URL

```
http://localhost:4000/api/flask
```

### Test Route

**GET** `/test`

- Response: `{ "message": "The server is running" }`

### Create User

**POST** `/users`

- Request Body:

```
{
  "name": "John Doe",
  "email": "johndoe@example.com"
}
```

- Response:

```
{
  "id": 1,
  "name": "John Doe",
  "email": "johndoe@example.com"
}
```

### Get All Users

**GET** `/users`

- Response:

```
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "johndoe@example.com"
  }
]
```

### Get User by ID

**GET** `/users/<id>`

- Response:

```
{
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "johndoe@example.com"
  }
}
```

### Update User

**PUT** `/users/<id>`

- Request Body:

```
{
  "name": "John Updated",
  "email": "johnupdated@example.com"
}
```

- Response:

```
{
  "message": "user updated"
}
```

### Delete User

**DELETE** `/users/<id>`

- Response:

```
{
  "message": "user deleted"
}
```

---

## Environment Variables

**Defined in `docker-compose.yml`:**

- `DATABASE_URL`: PostgreSQL connection string for Flask.
- `POSTGRES_USER`: Database username.
- `POSTGRES_PASSWORD`: Database password.
- `POSTGRES_DB`: Database name.

---

## Database Persistence

Data is persisted using a Docker volume:

```
volumes:
  pgdata:
```

This ensures data is not lost when the container restarts.

---

## Stopping the Application

To stop the containers, run:

```
docker-compose down
```

To remove all volumes (including database data):

```
docker-compose down -v
```

---

## License

This project is licensed under the [MIT License](LICENSE).
