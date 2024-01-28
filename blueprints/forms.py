from collections.abc import Mapping, Sequence
from typing import Any
import wtforms
from wtforms.validators import Email,Length,EqualTo, InputRequired
from models import UserModel,EmailCaptchaModel
from extensions import db


# Form : to verify if the data from front end is in right format
class RegisterForm(wtforms.Form):
    email    = wtforms.StringField(validators=[Email(message="Email Format Wrong!")])
    capthca  = wtforms.StringField(validators=[Length(min =4,max =4,message="Wrong validation code format!")])
    username = wtforms.StringField(validators=[Length(min =3,max =20,message="Wrong username format!")])
    password = wtforms.StringField(validators=[Length(min =6,max =20,message="Wrong password format!")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])

    #self-define:
    #1.if the email has been registered
    

    def validate_email(self,field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="The email has been registered!")
        
    #2.if the validation code is right
    def validate_captcha(self,field):
        captcha = field.data
        email = self.email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email,captcha=captcha).first()
        if not captcha_model:
            raise wtforms.ValidationError(message="Email or validation")
        #todo：可以删除captcha_model
        else:
            db.session.delete(captcha_model)
            db.session.commit()

    #另外的方法是写一个脚本，定期清理数据库（一周清理一次）
    #一个网站的瓶颈就是和数据库打交道，太平凡，没有必要的就不要去做，
            
    
class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误！")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误！")])


class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[Length(min=3, max=100, message="标题格式错误！")])
    content = wtforms.StringField(validators=[Length(min=3,message="内容格式错误！")])


class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[Length(min=3, message="内容格式错误！")])
    question_id = wtforms.IntegerField(validators=[InputRequired(message="必须要传入问题id！")])