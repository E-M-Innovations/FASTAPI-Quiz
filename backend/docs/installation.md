## Installation

```sh

# Install Virtual Env
$ pip install virtualenv

# move to backend directory
$ cd backend

# Create Virtual Environment
$ py -3 -m venv quiz-venv

# Activate Virtual Env [Windows]
$ .\quiz-venv\Scripts\activate

# Activate Virtual Env [Linux]
$ source quiz-venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Start server
$ uvicorn app.main:app --host 0.0.0.0 --port ${PORT} --reload

# Access
$ http://localhost:${PORT}

# Using Docker
$ docker-compose --env-file ./backend/.env build 

# Start
$ docker-compose --env-file ./backend/.env up

# Access
$ http://localhost:${PORT}

```