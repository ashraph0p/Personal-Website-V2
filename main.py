import os

from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor, CKEditorField
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap5(app)
ckeditor = CKEditor(app)
app.config['SECRET_KEY'] = os.environ['SECRET']


class job_req(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    message = CKEditorField('Message', validators=[DataRequired()])
    submit = SubmitField(validators=[DataRequired()])


@app.route("/", methods=["POST", "GET"])
def home():
    form = job_req()
    if form.validate_on_submit():
        data = {
            "Name": form.name.data,
            "Subject": form.subject.data,
            "Email": form.email.data,
            "Message": form.message.data}
        return redirect(
            f"mailto:m.ashraphx@gmail.com?subject={data['Subject']} -{data['Name']}&body={data['Message']}\n"
            f"from: {data['Email']}.")
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
