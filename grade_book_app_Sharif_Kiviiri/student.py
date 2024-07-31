#!/usr/bin/env python3

class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = None

    def register_for_course(self, course):
        self.courses_registered.append(course)

    def calculate_GPA(self):
        if not self.courses_registered:
            self.GPA = 0.0
            return self.GPA
        
        total_credits = 0
        total_points = 0

        for course in self.courses_registered:
            if course.grade is not None:
                total_credits += course.credits
                total_points += course.credits * course.grade

        if total_credits > 0:
            self.GPA = total_points / total_credits
        else:
            self.GPA = 0.0

        return self.GPA
