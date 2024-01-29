
SECRET_KEY = "asdfasdfjasdfjasd;lf"

# 数据库的配置信息
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'my_forum'
USERNAME = 'root'
PASSWORD = 'ql010203'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI


# 邮箱配置
MAIL_SERVER = "smtp.fastmail.com"
MAIL_PORT = 465
MAIL_USERNAME = "qinlong@fastmail.com"
MAIL_PASSWORD = "kj9qqc6q74pw863d"
MAIL_USE_TLS = False
MAIL_USE_SSL = True