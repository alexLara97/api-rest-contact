from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALQUEMY_DATABASE_URI"] = "sqlite://contacts.db"
db = SQLAlchemy(app)
