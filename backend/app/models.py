from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, AnonymousUserMixin
from sqlalchemy import CheckConstraint
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib

from . import db
