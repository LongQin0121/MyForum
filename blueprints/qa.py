from flask import  Blueprint,render_template

bp  =  Blueprint("qa",__name__,url_prefix="/")   # not"/qa

# http://127.0.0.1:5000
@bp.route("/")
def index():
    return render_template("index.html")