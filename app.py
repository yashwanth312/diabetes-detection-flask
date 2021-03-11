from flask import Flask 
from flask import render_template
from flask import request
import subprocess

app = Flask("ML_App")
#app.run(host="0.0.0.0")
@app.route("/")
def main():
    home_page = render_template("create.html")
    return home_page
@app.route("/prediction" , methods=["GET"])
def prediction():
    from keras.models import load_model
    model=load_model("mymodel-diabetes.h5")
    a = request.args.get("a")
    b = request.args.get("b")
    c = request.args.get("c")
    d = request.args.get("d")
    e = request.args.get("e")
    f = request.args.get("f")
    g = request.args.get("g")
    h = request.args.get("h")
    value  = model.predict([[float(a),float(b),float(c),float(d),float(e),float(f),float(g),float(h)]])
    final = int(value)
    if final == 1 :
        result = "You are detected POSITIVE for Diabetes"
    elif final == 0 :
        result = "You are detected NEGATIVE for Diabetes"
    return result

