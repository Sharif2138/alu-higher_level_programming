#!/usr/bin/env python3

class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = None

    def register_for_course(self, course):
        if course not in self.courses_registered:
            self.courses_registered.append(course)
        else:
            raise ValueError(f"Course {course.name} is already registered.")

    def assign_grade(self, course_name, grade):
        for course in self.courses_registered:
            if course.name == course_name:
                course.set_grade(self.email, grade)
                return
        raise ValueError(f"Course {course_name} not found for student {self.names}")

    def calculate_GPA(self):
        if not self.courses_registered:
            return 0.0
        
        total_credits = 0
        total_points = 0

        for course in self.courses_registered:
            grade = course.get_grade(self.email)
            if grade is not None:
                total_credits += course.credits
                total_points += course.credits * grade

        if total_credits > 0:
            self.GPA = total_points / total_credits
        else:
            self.GPA = 0.0
        
        return self.GPA
