from flask import Flask, jsonify, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-integers.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class NewInteger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Sensor Added {self.number}>"


# creating the db
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/<int:number>')
def save_number(number):
    print(type(number))
    new_sensor = NewInteger(number=number)
    db.session.add(new_sensor)
    db.session.commit()
    return f"<h1> {number} is Added to the Database. </h1>"


@app.route("/view-db")
def view_db():
    all_integers = db.session.query(NewInteger).all()
    print(type(all_integers))
    return render_template("numbers.html", integers=all_integers)


if __name__ == '__main__':
    app.run(debug=True)
