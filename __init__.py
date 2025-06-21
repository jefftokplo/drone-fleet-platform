from flask import Flask
from routes import api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://droneuser:dronepass@db:5432/dronefleet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api.init_app(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

