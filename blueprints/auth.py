from flask import Blueprint,render_template,jsonify
from extensions import mail,db
from flask_mail import Message
from flask import request
import string
import random
from models import EmailCaptchaModel

bp = Blueprint("auth",__name__,url_prefix="/auth")

@bp.route("/login")
def login():
    #pass
    return render_template("login.html")


@bp.route("/register")
def register():
    return render_template("register.html")

# bp.route:如果没有指定method，默认是GET请求 ，，POST
@bp.route("/captcha/email")
def get_email_captcha():
    #/captcha/email/<email>
    # /captcha/email?email = xxx@qq.com   传参
    email = request.args.get("email")
    #4/6 random
    source = string.digits * 4
    captcha = random.sample(source,4)
    #print(captcha)   ['6', '6', '1', '0']
    captcha = "".join(captcha)
    # message = Message(subject = "Validation Code for register",
    #                   recipients=[email],
    #                   body=f"Your validation Code is:{captcha}")
    # mail.send(message)

    msg = Message(  # Use Message class instead of EmailMessage
        "Validation Code for register",
        sender="qinlong@fastmail.com",
        recipients=[email],
    )
    msg.body = f"Your validation Code is:{captcha}"
    mail.send(msg)
    # memcached/redis
    # use database to store数据库
    email_captcha = EmailCaptchaModel(email=email,captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    #RESTful API
    #{code:200/400/500,message:"",data:{}}
    #return "success"
    return jsonify({"code":200,"message":"","data":None})    #发送邮件到后端

@bp.route("/mail/test")
def mail_test():
    # message = Message(subject="emailTest",recipients=["842857200@qq.com"],body="This is a test message")
    # mail.send(message)
    msg = Message(  # Use Message class instead of EmailMessage
        "Here is the title",
        sender="qinlong@fastmail.com",
        recipients=["qinlong0121@gmail.com"],
    )
    msg.body = "This is saturday_1-27"
    mail.send(msg)
    return "Email send successful"