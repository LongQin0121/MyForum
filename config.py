# Database configuration information
SECRET_KEY = "asdfasdfjasdfjasd;lf"


HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'my_forum'
USERNAME = 'root'
PASSWORD = 'ql010203'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

MAIL_SERVER = "smtp.fastmail.com"
MAIL_PORT = 465
MAIL_USERNAME = "qinlong@fastmail.com"
MAIL_PASSWORD = "kj9qqc6q74pw863d"
MAIL_USE_TLS = False
MAIL_USE_SSL = True


# Email configuration settings
# MAIL_SEVER = "smtp.qq.com"
# MAIL_USE_SSL = True
# MAIL_PORT = 465
# MAIL_USERNAME = "842857200@qq.com"
# MAIL_PASSWORD = "ql010203"
# MAIL_DEFAULT_SENDER = "842857200@qq.com"

# LULOHISKEZJMCLTI      163旧

#PBVCUVJUNYBOKEVV       163新
#  nxhfaqfcwfnibfid      qq