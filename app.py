from flask import Flask, render_template, send_file
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired
from cryptography.fernet import Fernet
import pandas

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")


@app.route('/', methods=['GET', "POST"])
@app.route('/home', methods=['GET', "POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        fernet = Fernet(b'9cVYDlqshER_Rg2zLQR_huBPKAilATrncGiFnSzkBns=')
        code = []
        number = []

        while True:
            f = file.readline()
            if not f:
                break
            code.append(f)
            number.append(fernet.decrypt(f).decode())
        db = pandas.DataFrame({'Before': code,
                               "After:": number})
        db.to_excel('static/file.xlsx')

        return send_file('static/file.xlsx')

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
