from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import Student

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        math_score = int(request.form['math_score'])
        science_score = int(request.form['science_score'])
        english_score = int(request.form['english_score'])

        new_student = Student(name=name, math_score=math_score, science_score=science_score, english_score=english_score)
        db.session.add(new_student)
        db.session.commit()

        flash('Student added successfully!', 'success')
        return redirect(url_for('main.performance'))

    return render_template('add_student.html')

@main.route('/performance')
def performance():
    students = Student.query.all()
    class_average = (
        sum(student.calculate_average() for student in students) / len(students) if students else 0
    )
    return render_template('performance.html', students=students, class_average=class_average)

@main.route('/edit_student/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)

    if request.method == 'POST':
        student.name = request.form['name']
        student.math_score = int(request.form['math_score'])
        student.science_score = int(request.form['science_score'])
        student.english_score = int(request.form['english_score'])

        db.session.commit()
        flash('Student updated successfully!', 'success')
        return redirect(url_for('main.performance'))

    return render_template('edit_student.html', student=student)

@main.route('/delete_student/<int:id>')
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()

    flash('Student deleted successfully!', 'success')
    return redirect(url_for('main.performance'))
