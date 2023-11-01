from flask import Flask,render_template,request,jsonify

app = Flask(__name__)


@app.route("/")
def home():
    data = request.args.get('x')
    return data

@app.route("/wel/<name>")
def welcome(name):
    
    return f"welcome {name}"



if __name__ == "__main__":
    app.run("0.0.0.0",port=5002)