from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib

from . import db

class User(db.Model):
    __tablename__ = 'User'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)                                           
    Name = db.Column(db.String(255), nullable=False)                                                           
    Mail = db.Column(db.String(255), nullable=False, unique=True, index=True)                                  
    Service_ID = db.Column(db.Integer)                            
    ProfilePIC = db.Column(db.String(255))                                                                     
    About_Me = db.Column(db.Text, nullable=True)                                                               
    Date_Created = db.Column(db.DateTime, default=db.func.now())                                               
    Password_hash = db.Column(db.String(255), nullable=False)                                                  

    def to_json(self):

        json_project = {
            'ID': self.ID,
            'Name': self.Name,
            'Mail': self.Mail,
            'Service_ID': self.Service_ID,
            'ProfilePIC': self.ProfilePIC,
            'About_Me': self.About_Me,
            'Date_Created': self.Date_Created,
        }

        return json_project

    def __repr__(self):
        return "User: {} [{}]".format(self.Name, self.ID)
    
    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.Password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.Password_hash, password)
    
    def get_id(self):
        return self.ID

    def is_user(self):
        return not (self.is_admin())
    
    def is_admin(self):
        if self.Mail == "admin@admin.net":
            return True
        return False

    user_in_groups = db.relationship('UserInGroup', backref='user')
    

class Project(db.Model):
    __tablename__ = 'Project'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Project_Name = db.Column(db.String(255), nullable=False)    
    Project_Status = db.Column(db.String(20), nullable=False, default='Incomplete')
    Project_Percentage = db.Column(db.Integer)
    Date_Created = db.Column(db.DateTime, default=db.func.now())
    Custom_Status = db.Column(db.Text, nullable=True)
    Project_Deadline = db.Column(db.DateTime, nullable=False)
    Project_Budget = db.Column(db.Integer)
    Project_Budget_Remaining = db.Column(db.Integer)
    Project_Tags = db.Column(db.Text, nullable=True)
    Description = db.Column(db.Text, nullable=True)

    CheckConstraint("Project_Status IN ('Incomplete', 'Completed', 'On Hold')")
    CheckConstraint("Project_Percentage BETWEEN 10 AND 20")

    def to_json(self):

        json_project = {
            'ID': self.ID,
            'Project_Name': self.Project_Name,
            'Project_Status': self.Project_Status,
            'Project_Percentage': self.Project_Percentage,
            'Date_Created': self.Date_Created,
            'Description': self.Description,
            'Project_Budget': self.Project_Budget,
            'Project_Budget_Remaining': self.Project_Budget_Remaining,
            'Project_Deadline': self.Project_Deadline,
            'Project_Tags': self.Project_Tags,
            'Custom_Status': self.Custom_Status
        }

        return json_project
    
    def __repr__(self):
        return "Project: {} [{}]".format(self.Project_Name, self.ID)

    user_in_groups = db.relationship('UserInGroup', backref='project')

class UserInGroup(db.Model):
    __tablename__ = 'UserInGroup'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    User_ID = db.Column(db.Integer, db.ForeignKey('User.ID'), nullable=False)
    Project_ID = db.Column(db.Integer, db.ForeignKey('Project.ID'), nullable=False)
    Admin = db.Column(db.Integer, default=False, nullable=False) 
    
    __table_args__ = (db.UniqueConstraint('User_ID', 'Project_ID', name='unique_user_project'),)

class Tasks(db.Model):
    __tablename__ = 'Tasks'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    User_ID = db.Column(db.Integer, db.ForeignKey('User.ID'), nullable=False)
    Project_ID = db.Column(db.Integer, db.ForeignKey('Project.ID'), nullable=False)
    Task_Status = db.Column(db.String(20), nullable=False, default='Incomplete')
    Date_Created = db.Column(db.DateTime, default=db.func.now())
    Date_Deadline = db.Column(db.DateTime)
    Custom_Status = db.Column(db.Text, nullable=True)
    Budget_Allocated = db.Column(db.Integer)
    Task_Tags = db.Column(db.Text, nullable=True)
    Task_Priority = db.Column(db.Integer)

    CheckConstraint("Task_Status IN ('Incomplete', 'Completed', 'On Hold')")

class Message(db.Model):
    __tablename__ = 'MessageInGroup'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    User_ID = db.Column(db.Integer, db.ForeignKey('User.ID'), nullable=False)
    Project_ID = db.Column(db.Integer, db.ForeignKey('Project.ID'), nullable=False)
    Task_ID = db.Column(db.Integer, db.ForeignKey('Tasks.ID'), nullable=False)
    Date_Created = db.Column(db.DateTime, default=db.func.now())                                                                
    Text = db.Column(db.Text, nullable=False)  

class FinancialRecord(db.Model):
    __tablename__ = 'FinancialRecord'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Project_ID = db.Column(db.Integer, db.ForeignKey('Project.ID'), nullable=False)
    Expense = db.Column(db.Boolean)
    Amount = db.Column(db.Integer)
    Date_Created = db.Column(db.DateTime, default=db.func.now())                                                                
    Reason = db.Column(db.Text, nullable=False)  








