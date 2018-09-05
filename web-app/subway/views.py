from flask import render_template, request
from subway import app
from subway.forms import SandwichForms

@app.route('/')
def toppage():
    form = SandwichForms(request.form)
    title='Play Sandwich'
    return render_template(
        'index.html',
        title=title,
        form=form
    )


@app.route('/result')
def result():
    title='Play Sandwich'
    return render_template(
        'result.html',
        title=title)
