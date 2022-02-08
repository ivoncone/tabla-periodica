from flask import Flask, render_template, url_for

app = Flask(__name__)

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
def table():
	return render_template("table.html", elements=elements)