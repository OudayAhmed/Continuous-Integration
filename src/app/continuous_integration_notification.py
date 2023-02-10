from flask import request, Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/send_message', methods=['GET', 'POST'])
def send_message(email, syntax, testing):
    """
    Method to send message through email with with build results to user email
    :returns: Result of build
    """
    if request.method == "POST":
        subject = "Build Results."
        msg = str(syntax) + "\n" + str(testing) ## request.form['message'] ## Read and write the build results as the message
        message = Message(subject, sender="cigroup15vt23@gmail.com", recipients=[email])
        message.body = msg
        mail.send(message)
        success = "Message sent"
        return render_template("results.html", success=success)
