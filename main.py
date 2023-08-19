from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditor, CKEditorField
from flask_bootstrap import Bootstrap5
import os

app = Flask(__name__)
bootstrap = Bootstrap5(app)
ckeditor = CKEditor(app)
app.config['SECRET_KEY'] = os.environ['SECRET']


class job_req(FlaskForm):
    name = StringField(validators=[DataRequired()])
    email = EmailField(validators=[DataRequired()])
    message = CKEditorField(validators=[DataRequired()])
    submit = SubmitField(validators=[DataRequired()])


@app.route("/")
def home():
    form = job_req()
    if form.validate_on_submit():
        pass
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
