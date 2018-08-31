from flask import render_template
from subway import app


@app.route('/')
def toppage():
    title='Play Sandwich'
    return render_template(
        'index.html',
        title=title
    )


@app.route('/result')
def result():
    title='Play Sandwich'
    return render_template(
        'result.html',
        title=title)
