import flask
import random
import hashlib
import os
import logging

app = flask.Flask(__name__)

@app.route('/')
def root():
    return flask.render_template('index.html')    

@app.route('/p/<requested_page>')
def templater(requested_page):
    return flask.render_template(requested_page)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)