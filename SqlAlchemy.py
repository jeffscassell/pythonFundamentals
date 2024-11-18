import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



#=================
# Flask-SQLAlchemy
#=================

app = Flask("SQLAlchemy Testing")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"
database = SQLAlchemy(app)



class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(20), unique=True, nullable=False)
    password = database.Column(database.String(45), nullable=False)
    
    # not an actual column. references the class, so note the capital "Post." creates an ORM quasi-column that can be used on Post
    # to access the entire User object
    # the lazy keyword signifies that when fetching the object, it will also fetch all of the associated objects (Posts in this case)
    posts = database.relationship("Post", backref="author", lazy=True)  # one-to-many relationship
    
    def __repr__(self):
        return f"ID: {self.id}, {self.username}"
    
    
class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(50), nullable=False)
    datePosted = database.Column(database.DateTime, nullable=False, default=datetime.datetime.now(datetime.timezone.utc))
    
    # IS an actual column, so references the table, which is automatically created/converted to snake_case. note the "user.id"
    userId = database.Column(database.Integer, database.ForeignKey("user.id"), nullable=False)
    
    def __repr__(self):
        return f"{self.title}"
    
    
    
if (__name__ == "__main__"):
    app.run(debug=True)