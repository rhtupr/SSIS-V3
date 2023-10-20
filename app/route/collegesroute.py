from flask import * 
from app.models.colleges import *
from flask_wtf import *

colleges_bp = Blueprint ('colleges', __name__)

@colleges_bp.route('/colleges/')
def college():
    colleges = collegeread()
    return render_template('colleges.html', colleges=colleges)

@colleges_bp.route('/colleges/add', methods=['GET', 'POST'])
def add_college():
    if request.method == 'POST':
        collegecode = request.form['collegecode']
        collegename = request.form['collegename']
        print(collegecode, collegename)
        add_col(collegecode, collegename)
        return redirect('/colleges') 
    return render_template('colleges.html')

@colleges_bp.route('/colleges/search', methods=['GET', 'POST'])
def search_colleges():
    colleges = []
    if request.method == 'POST':
        search_query = request.form.get('search_college')
        if search_query:
            colleges = find_colleges(search_query)
    return render_template('colleges.html', colleges=colleges)

@colleges_bp.route('/colleges/delete/<string:collegecode>', methods=['DELETE'])
def remove_college(collegecode):
    if request.method == 'DELETE':
        print(collegecode)
        delete_college(collegecode)
        return jsonify({'success': True})
    
@colleges_bp.route('/colleges/edit', methods=['POST'])
def edit_college():
    if request.method == 'POST':
        college_code = request.form.get('college_code').upper()
        college_name = request.form.get('college_name')
        update_college(college_code, college_name)
        return redirect('/colleges/')
    

