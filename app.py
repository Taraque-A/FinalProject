import pip
import requests
from flask import flask, request, jsonify, make_response, Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('MovieTitles.html')


@app.route("/Receipt")
def receipt():
    return render_template('Receipt.html')
    


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'Click to See Descriptions':
            return render_template("Receipt.html") #This will be for Movie Descriptions


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
