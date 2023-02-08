from flask import request, Flask, render_template
from flask_mail import Mail, Message

from continuous_integration import ContinuousIntegration
from repo_github import RepoGitHub
import os

team_dict = {}
team_dict['OudayAhmed'] = "oydddua@gmail.com"
team_dict['ChristoferVikstroem'] = "christofer.vikstrom@outlook.com"
team_dict['eliu1217'] = "elin.liu@hotmail.se"
team_dict['OscarKnowles'] = "Oscar@knowles.se"
team_dict['Taomyee'] = "yimingju2000@gmail.com"

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_POST'] = 465
app.config['MAIL_USERNAME'] = "cigroup15vt23@gmail.com"
app.config['MAIL_PASSWORD'] = "contintg15"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


@app.route('/')
def index():
    return render_template("home.html")

@app.route('/send_message', methods=['GET', 'POST'])
def send_message():
    if request.method == "POST":
        email = request.form['email']
        subject = request.form['subject']
        msg = request.form['message']
        message = Message(subject, sender="cigroup15vt23@gmail.com", recipients=[email])
        message.body = msg
        mail.send(message)
        success = "Message sent"
        return render_template("results.html", success=success)


if __name__ == "__main__":
    app.run(host='localhost', port=8015)
