from flask import Flask, render_template, redirect, request
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
import smtplib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!Really'
Bootstrap(app)

MY_EMAIL = "elrondduma@gmail.com"
MY_PASSWORD = "2xTw5h8imu4uYES"
TO_EMAIL = "ozturknuri8@gmail.com"

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


@app.route("/")
def home():
    date = datetime.now()
    date3 = date.year
    return render_template("index.html", year=date3)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        data = request.form
        contents = data["name"]+"\n"+data["email"] + "\n" + data["message"]
        contents = contents.encode("utf-8")
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg=f"Subject:New Contact!\n\n{contents}"
            )
        return render_template("success.html")
    return render_template("contact.html", form=form)


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)



