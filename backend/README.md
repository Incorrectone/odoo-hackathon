# Backend part of the project

## Install Dpendencies and Project Setup
> pip instal -r requirements.txt

### Run the project
> export FLASK_APP = hbodoo.py
> flask run [-debug]

### Create Database from models:
> flask shell
> from app.models import db
> db.create_all()
> db.session.commit()
