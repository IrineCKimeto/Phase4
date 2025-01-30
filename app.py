import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

db = SQLAlchemy()


app = Flask(__name__)
CORS(app)

    
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    
db.init_app(app)

with app.app_context():
    from models import User, Book, Review  
    db.create_all()

    
from routes import api_routes
app.register_blueprint(api_routes)

if __name__ == "__main__":
    app.run(debug=True)