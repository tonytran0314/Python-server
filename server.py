#Server file

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/details")
def detls():
    return "This is details page"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
