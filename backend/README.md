# Backend part of the project

## Install Dependencies and Project Setup
> pip install -r requirements.txt

### Run the project
> export FLASK_APP = hbodoo.py
> flask run [-debug]

### Create Database from models:
> flask shell
> from app.models import db
> db.create_all()
> db.session.commit()
