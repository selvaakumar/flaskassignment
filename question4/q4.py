from flask import Flask,render_template,request,jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/math',methods = ['POST'])
def calculator():
    ops  = request.form['operation']
    num1  = int(request.form['num1'])
    num2  = int(request.form['num1'])
    print(f"{ops} {num1} {num2}")

    if ops == 'add':
        return f"addion of {str(num1)} and {str(num2)} is {str(num1 + num2)}"

    if ops == 'subtract':
        return f"subtract of {num1} and {num2} is {num1 - num2}"
    
    if ops == 'multiply':
        return f"multiply of {num1} and {num2} is {num1 * num2}"
    
    if ops == 'divide':
        return f"divide of {num1} and {num2} is {num1 / num2}"





if __name__=="__main__":
    app.run(host="0.0.0.0",port=5003)