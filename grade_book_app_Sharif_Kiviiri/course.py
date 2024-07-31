#!/usr/bin/env python3
class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits
        self.grade =  None

     def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.grade = grade
        else:
            raise ValueError("Grade must be between 0 and 100.")
    
