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
        college_code = request.form['collegecode']
        college_name = request.form['collegename']
        if check(college_code):
            flash('College Code already exists!', 'error')
        elif len(college_code)> 20:
            flash('College Code too long!', 'error')
        else:
            insert_college(college_code, college_name)
            return redirect('/colleges') 
    return render_template('addcollege.html')


@colleges_bp.route('/colleges/editcollege', methods=['GET', 'POST'])
def edit_college():
    if request.method == 'POST':
        # Handle the POST request to update the college information in your database
        college_code = request.form.get('college_code')
        new_college_name = request.form.get('college_name')
        
        # Update the college information in the database
        update_college(college_code, new_college_name)  # Call the update_college function

        # Redirect to the colleges page
        return redirect('/colleges')
    else:
        # Handle the GET request (render the edit form)
        collegecode = request.args.get('collegecode')
        collegename = request.args.get('collegename')
        return render_template('editcollege.html', college_code=collegecode, college_name=collegename)


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
    


