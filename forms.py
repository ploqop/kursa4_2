from wtforms.form import Form
from wtforms import StringField, SubmitField, BooleanField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError, Regexp


class MyForm(Form):
    email = StringField("Email: ", validators=[])
    password = PasswordField("Пароль: ", validators=[DataRequired(), Length(min=4, max=20)])
    remember = BooleanField("Запомнить", default=False)
    submit = SubmitField("Войти")


class PrimeForm(Form):
    number = IntegerField("Число: ", validators=[DataRequired(), Length(max=6), NumberRange(min=1, max=999999)])
    submit = SubmitField("Проверить: ")
