from flask import * 
from app.models.colleges import *
from flask_wtf import *

colleges_bp = Blueprint ('colleges', __name__)

@colleges_bp.route('/colleges/')
def college():
    colleges = collegeread()
    return render_template('colleges.html', colleges=colleges)

@colleges_bp.route('/colleges/', methods=['GET', 'POST'])
def add_college():
    if request.method == 'POST':
        collegecode = request.form['collegecode']
        collegename = request.form['collegename']
        add_col(collegecode, collegename)
        return redirect('/colleges') 
    return render_template('colleges.html')
