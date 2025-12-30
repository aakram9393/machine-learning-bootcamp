from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the Machine Learning Course Flask App! thanks for visiting.Again"

@app.route("/index")
def index():
    return "welcome to index page"


if __name__ == "__main__":
    app.run(debug=True)