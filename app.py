"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
from flask import Flask, render_template, request
from flask.wrappers import Request
import webbrowser

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

Sort_to_Long_URL = {}
count = 0

@app.route('/')
def root():
    return render_template("index.html")
@app.route('/sort_URL',methods=['GET', 'POST'])
def sort_URL():
    global Sort_to_Long_URL,count
    if request.method=="POST":
        longUrl =request.form['LongURL']
        count+=1
        C = str(count)
        Sort_to_Long_URL[C] = longUrl
            
    return render_template("index.html",longURL=longUrl,sortURL=("http://localhost:5555/go?sortURL="+str(count)))
@app.route('/go',methods=['GET'])
def go():
    global Sort_to_Long_URL,count
    if request.method=="GET":
        key = request.args['sortURL']
        URL = Sort_to_Long_URL[key]

    return render_template("index.html",URL=URL);
if __name__ == '__main__':
    import os
    webbrowser. open('http://localhost:5555')
    app.run('localhost',port='5555')