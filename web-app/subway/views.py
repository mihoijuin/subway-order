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

@app.route('/result', methods = ['POST'])
def result():
    title='Play Sandwich'
    vege_list = ['lettus', 'tomato', 'green', 'onion', 'carrot', 'olive', 'pickles', 'hot']
    if request.form:
        user_sand = request.form['sand']
        user_bread = request.form['bread']
        user_toppings = request.form.getlist('topping')
        vege_amounts = [ request.form[i] for i in vege_list]
        user_souces = request.form.getlist('source')
        return render_template(
            'result.html',
            title=title,
            user_sand=user_sand,
            user_bread=user_bread,
            user_toppings=user_toppings,
            vege_amounts=vege_amounts,
            user_souce=user_souces
            )
