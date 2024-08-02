#!/usr/bin/env python3

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, student):
        self.student_list.append(student)

    def add_course(self, course):
        self.course_list.append(course)

    def register_student_for_course(self, student, course):
        if student in self.student_list and course in self.course_list:
            student.register_for_course(course)
        else:
            raise ValueError("Student or Course not found.")

    def calculate_GPA(self, student):
        return student.calculate_GPA()

    def calculate_ranking(self):
        sorted_students = sorted(self.student_list, key=lambda student: student.GPA if student.GPA else 0, reverse=True)
        return sorted_students

    def search_by_grade(self, grade):
        matching_students = []
        for student in self.student_list:
            for course in student.courses_registered:
                if course.grade == grade:
                    matching_students.append(student)
                    break
        return matching_students

    def generate_transcript(self, student):
        if student in self.student_list:
            transcript = f"Transcript for {student.names}:\n"
            transcript += f"Email: {student.email}\n"
            transcript += "Courses Registered:\n"
            for course in student.courses_registered:
                transcript += f"- {course.name}, Trimester: {course.trimester}, Credits: {course.credits}, Grade: {course.grade}\n"
            transcript += f"GPA: {student.GPA}\n"
            return transcript
        else:
            raise ValueError("Student not found.")
