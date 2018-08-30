from flask import render_template
from subway import app

@app.route('/')
def toppage():
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')