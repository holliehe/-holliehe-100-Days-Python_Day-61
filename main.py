#522
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import ValidationError, Email, InputRequired, Length
import os

SECRET_KEY =os.urandom(32)

app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = SECRET_KEY

class MyForm(FlaskForm):
    email = EmailField(label='Email', validators=[Email(), InputRequired("Input required.")])
    password = PasswordField(label='Password', validators=[InputRequired("Input required."),
                                                           Length(min=8, message=f"Feild must be at least 8 characters long.")])
    submit = SubmitField(label="Log In")


@app.route("/", methods=["GET", "POST"])
def cafe():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data=="admin@email.com" and form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('cafe.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)


#514-521
"""from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import ValidationError, Email, InputRequired, Length
import os
from flask_bootstrap import Bootstrap

SECRET_KEY =os.urandom(32)

app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
def home():
    return render_template('index.html')


class MyForm(FlaskForm):
    email = EmailField(label='Email', validators=[Email(), InputRequired("Input required.")])
    password = PasswordField(label='Password', validators=[InputRequired("Input required."),
                                                           Length(min=8, message=f"Feild must be at least 8 characters long.")])
    submit = SubmitField(label="Log In")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data=="admin@email.com" and form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)"""