from flask import render_template
from flask.ext.mail import Message
from app import app, mail
from config import ADMINS
from .decoretors import async


@async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, recipients=recipients, sender=sender)
    msg.body = text_body
    msg.html = html_body
    send_async_email(app, msg)


def follower_notification(followed, follower):
    send_mail("[microblog] %s is now following you!" % follower.nickname,
              ADMINS[0],
              [followed.email],
              render_template('follower_email.txt', user=followed, follower=follower),
              render_template('follower_email.html', user=followed, follower=follower))
