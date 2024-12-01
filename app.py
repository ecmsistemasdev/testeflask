from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/inscricao")
def inscricao():
    return render_template("inscricao.html")

@app.route("/insc")
def insc():
    return render_template("insc.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

if __name__ == "__main__":
    app.run(debug=True)

