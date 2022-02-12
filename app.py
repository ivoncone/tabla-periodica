from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
import sys 
import os
import uuid as uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = "me gustan las manzanas"
app.debug=True

# Create database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///elements.db'

db = SQLAlchemy(app)

# Create model
class Elements(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	symbol = db.Column(db.String(200), nullable=False)
	name = db.Column(db.String(100), nullable=False)
	atomic_number = db.Column(db.Integer)
	atomic_weight =  db.Column(db.Integer)

	def __repr__(self):
		return '<Name %r>' % self.name

class ElementsForm(FlaskForm):
	symbol = StringField("symbol")
	name = StringField("Name")
	atomic_number = StringField("atomic number")
	atomic_weight = StringField("atomic weight")
	submit = SubmitField("submit")


# Dummy Array
elements = (
	("Litio", "Li"),
	("Hidrogeno", "H"),
	("Berilio", "Be"),
	("Sodio", "Na"),
	("Magnesio", "Mg"), 
	("Potasio", "K"),
	("Calcio", "Ca"),
	("Escandio","Sc"),
	("Titanio", "Ti"),
	("Vanadio", "V"),
	("Cromo", "Cr"),
	("Manganeso", "Mn"),
	("Hierro", "Fe"),
	("Cobalto", "Co"),
	("Niquel", "Ni"),
	("Cobre", "Cu"),
	("Zinc", "Zn"),
	("Garlio", "Ga"),
	("Boro", "B")
	)

@app.route("/")
def index():
	elements = Elements.query.order_by(Elements.atomic_number)
	return render_template("index.html", elements=elements)

@app.route('/element/add', methods=['GET', 'POST'])
def add_element():
	form = ElementsForm()
	if form.validate_on_submit():
		element = Elements(symbol=form.symbol.data, name=form.name.data, atomic_number=form.atomic_number.data, atomic_weight=form.atomic_weight.data)
		form.symbol.data = ''
		form.name.data = ''
		form.atomic_number = ''
		form.atomic_weight.data = ''

		db.session.add(element)
		db.session.commit()
	return render_template("add_element.html", form=form)

