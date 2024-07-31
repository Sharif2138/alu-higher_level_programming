#!/usr/bin/env python3
class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits
        self.grade =  None

    def set_grade(self, grade):
        if 0 <= grade <= 100:  # Assuming grade is out of 100
            self.grade = grade
        else:
            print("Grade must be between 0 and 100.")
    
    def get_grade(self):
        return self.grade
    
    def __str__(self):
        return (f"Course: {self.name}\n"
                f"Trimester: {self.trimester}\n"
                f"Credits: {self.credits}\n"
                f"Grade: {self.grade if self.grade is not None else 'Not assigned'}")

# Example usage
if __name__ == "__main__":
    course = Course("Introduction to Python", "Fall 2024", 3)
    print(course)
    course.set_grade(85)
    print(f"Grade: {course.get_grade()}")
    print(course)


