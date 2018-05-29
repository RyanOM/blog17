# blog17
Small WebBlog app written in Django 1.7
---

## Features:

- Images via Pillow
- Tags via Taggit


## Requirements

- Python2

## Instructions

Clone the app and access the folder:
```
git clone https://github.com/RyanOM/blog17.git
cd blog17
```

Create a virtualenv, activate it and install the depdencies:
```
virtualenv blog17
source blog17/bin/activate
pip install -r requirements.txt
```

Update the database and run the server:
```
python manage.py syncdb
python manage.py runserver
```

Access the webapp:
http://localhost:8000/
