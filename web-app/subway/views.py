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
    if request.form:
        user_sand = request.form['sand']
        user_bread = request.form['bread']
        user_toppings = request.form.getlist('topping')
        #! テンプレートに「〇〇の量：普通」表示する繰り返し処理が思いつかないため、暫定的に野菜も一個ずつ変数に格納
        lettus_amount = request.form['lettus']
        tomato_amount = request.form['tomato']
        green_amount = request.form['green']
        onion_amount = request.form['onion']
        carrot_amount = request.form['carrot']
        olive_amount = request.form['olive']
        pickles_amount = request.form['pickles']
        hot_amount = request.form['hot']
        user_sources = request.form.getlist('source')
        return render_template(
            'result.html',
            title=title,
            user_sand=user_sand,
            user_bread=user_bread,
            user_toppings=user_toppings,
            lettus_amount=lettus_amount,
            tomato_amount=tomato_amount,
            green_amount=green_amount,
            onion_amount=onion_amount,
            carrot_amount=carrot_amount,
            olive_amount=olive_amount,
            pickles_amount=pickles_amount,
            hot_amount=hot_amount,
            user_source=user_sources,
            )
