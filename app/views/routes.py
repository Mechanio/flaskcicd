from flask import request, Blueprint, render_template

from app.forms import MainForm


main_routes_bp = Blueprint("main_routes", __name__)


@main_routes_bp.route('/', methods=['GET', 'POST'])
def home():
    mainform = MainForm()
    if request.method == 'POST' and mainform.validate_on_submit():
        if request.form['submit_button'] == 'Submit':
            text = mainform.text.data
            upper_cased = text.upper()
            return render_template("home.html", mainform=mainform, upper_cased=upper_cased)
    return render_template("home.html", mainform=mainform)
