from flask import Flask, request, render_template, session, redirect, url_for
import os

app = Flask(__name__)





if __name__=="__main__":
    app.run(host="0.0.0.0",port=5005)