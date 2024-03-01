from django.shortcuts import render
import pandas as pd

def get_student_timetable(student_id):
    filename = f"entries/student{student_id}.csv"

    try:
        df = pd.read_csv(filename)
        return df[['Day', 'Time', 'Subject']]
    except FileNotFoundError:
        return None

def index(request):
    # Assuming student IDs are 1, 2, and 3
    student_ids = [1, 2, 3]
    student_timetables = {}

    for student_id in student_ids:
        student_timetables[student_id] = get_student_timetable(student_id)
        

    return render(request, 'schedule/index.html', {
        'student_timetables': student_timetables,
    })
