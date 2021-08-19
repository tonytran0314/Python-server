#Server file

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") # must have templates folder to contain html files

@app.route("/details")
def detls():
    return render_template("details.html")

@app.errorhandler(404)
def error():
    return render_template("error.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
