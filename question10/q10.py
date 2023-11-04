from flask import Flask, render_template

app = Flask(__name__)

# Custom error handlers for 404 and 500 errors
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error_404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error_500.html'), 500

# Route for a sample page
@app.route('/')
def index():
    return "Welcome to the Flask Error Handling Example"


@app.route('/not_found')
def not_found():
    abort(404)

# Trigger a 500 error
@app.route('/internal_error')
def internal_error():
    # This will raise an exception, simulating a server error
    a = 1 / 0

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8006)
