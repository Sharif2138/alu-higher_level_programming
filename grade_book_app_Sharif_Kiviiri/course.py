#!/usr/bin/env python3

class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits
        self.student_grades = {}  # Dictionary to track grades for each student

    def set_grade(self, student_email, grade):
        if 0 <= grade <= 100:
            self.student_grades[student_email] = grade
        else:
            raise ValueError("Grade must be between 0 and 100.")

    def get_grade(self, student_email):
        return self.student_grades.get(student_email, None)

