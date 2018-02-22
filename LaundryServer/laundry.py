# Don't forget:
# set APPSETTINGS=secrets.cfg
# turn off firewall

from flask import Flask, url_for, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config["MAIL_SERVER"]="smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
app.config.from_envvar("APPSETTINGS")

mail = Mail(app)

@app.route("/send/", methods=["GET", "POST"])
def send():
    print("Got something!")
    if request.method == "POST":
        try:
            address = request.form["address"]
            subject = request.form["subject"]
            message = request.form["message"]

            msg = Message(sender=("Network Everything", "mjmnetworkeverything@gmail.com"), recipients=[address], subject=subject, body=message, cc=["jiwon.kim@nyu.edu", "arz268@nyu.edu", "mshiloh@nyu.edu"])

            mail.send(msg)

            return "Yay Mail"
        except KeyError:
            return "oops"
    else:
        return "404"
