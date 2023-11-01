from flask import Flask,render_template,request,jsonify


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
   
   
@app.route("/page1")
def page1():
    return render_template('page1.html')

@app.route("/page2")
def page2():
    return render_template('page2.html')


if __name__ == "__main__":
    app.run("0.0.0.0",port=5001)