# integrate-django-and-vuejs

This project use Vue.JS to frontend and Django in backend. Its only a simple example how to integrate this two frameworks.

# First steps

## Clone this repository:

```bash
git clone https://github.com/2005869/integrate-django-and-vuejs.git
```

## Install dependencies and first settings:

### For Vue.JS

```bash
cd frontend/app/
npm install
```

### For Django

```bash
cd backend/

# create virtual environment
python3 -m venv env

# activate virtual environment
source env/bin/activate

# install requirements
pip install -r requirements.txt

# migrate
python3 manage.py migrate

# create a superuser
python3 manage.py createsuperuser
```

## Run the server

### For Vue.JS

```bash
cd frontend/app/
vue serve
```

### For Django

```bash
cd frontend/app/
python3 manage.py runserver
```

## Testing the project

In your favorite browser first access http://localhost:8000/admin and do login with your superuser, insert some data in database, this project have a simple model that contain only the fields **name** and **age** to fill. Go and insert some data and when you are satisfied go to http://localhost:8080 and you will see the data that you insert in Django show in a Vue.JS project.
