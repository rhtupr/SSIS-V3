function deleteCollege(button) {
    console.log("Delete button clicked.");
    var college_code = button.getAttribute('college-code');
    var csrfToken = button.getAttribute('csrf-token');
    if (confirm("Are you sure you want to delete this college?\nStudents and Courses under this College will also be deleted.")) {
        fetch(`/colleges/delete/${college_code}`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrfToken
            }
        }).then(response => response.json())
        .then(data => {
            if (data.success === true) {
                window.location.reload();
            } else {
                console.error("Error: " + data.error);
            }
        });        
    }
}


function deleteCourse(button) {
    console.log("Delete button clicked.");
    var course_code = button.getAttribute('course-code');
    var csrfToken = button.getAttribute('csrf-token');
    if (confirm("Are you sure you want to delete this college?\nStudents under this College will also be deleted.")) {
        fetch(`/courses/delete/${course_code}`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrfToken
            }
        }).then(response => response.json())
        .then(data => {
            if (data.success === true) {
                window.location.reload();
            } else {
                console.error("Error: " + data.error);
            }
        });        
    }
}

function deleteStudent(button) {
    console.log("Delete button clicked.");
    var stud_id = button.getAttribute('student-id');
    var csrfToken = button.getAttribute('csrf-token');
    if (confirm("Are you sure you want to delete this student?")) {
        fetch(`/students/delete/${stud_id}`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrfToken
            }
        }).then(response => response.json())
        .then(data => {
            if (data.success === true) {
                window.location.reload();
            } else {
                console.error("Error: " + data.error);
            }
        });        
    }
}
