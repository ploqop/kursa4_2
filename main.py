import math

from flask import Flask, flash, redirect, render_template, \
     request, url_for
import datetime
from forms import MyForm, PrimeForm

app = Flask(__name__)


@app.template_filter(name='is_prime')
def is_prime(n):
    if n == 2:
        return True
    for i in range(2, int(math.ceil(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True


@app.route('/', methods=["POST", "GET"])
@app.route('/index', methods=["POST", "GET"])
def index(number=None):
    date_one = datetime.date.__new__(datetime.date, 2022, 9, 2)
    date_two = datetime.date.__new__(datetime.date, 2022, 9, 2)
    form = MyForm()
    formPrime = PrimeForm(request.form)
    if request.method == 'POST':
        number = int(request.form['number'])
        form.validate()
        redirect(url_for('index', param=number, _anchor='bottom'))

    return render_template('index.html', text='Этот текст передан из контроллера', numbers=['1', '2', '3'],
                           date_one=date_one.strftime('%d/%m/%Y'), date_two=date_two, form=form, formPrime = formPrime,
                           number=number)


if __name__ == '__main__':
    app.run(debug=True)
