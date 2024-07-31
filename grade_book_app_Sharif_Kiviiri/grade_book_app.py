#!/usr/bin/env python3
from student import Student
from course import Course
from grade_book import GradeBook

def main():
    grade_book = GradeBook()

    while True:
        print("\nGrade Book Application")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Student Course Registration")
        print("4. Ranking")
        print("5. Search by Grade")
        print("6. Generate Transcript")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        try:
            if choice == '1':
                email = input("Enter student's email: ")
                names = input("Enter student's names: ")
                if not email or not names:
                    print("Error: Email and names cannot be empty.")
                    continue
                student = Student(email, names)
                grade_book.add_student(student)
                print("Student added successfully!")

            elif choice == '2':
                name = input("Enter course name: ")
                trimester = input("Enter trimester: ")
                try:
                    credits = int(input("Enter credits: "))
                    if credits <= 0:
                        raise ValueError("Credits must be a positive integer.")
                except ValueError:
                    print("Error: Credits must be a valid positive integer.")
                    continue
                course = Course(name, trimester, credits)
                grade_book.add_course(course)
                print("Course added successfully!")

            elif choice == '3':
                email = input("Enter student's email: ")
                course_name = input("Enter course name: ")

                student = next((s for s in grade_book.student_list if s.email == email), None)
                if student:
                    course = next((c for c in grade_book.course_list if c.name == course_name), None)
                    if course:
                        grade_book.register_student_for_course(student, course)
                        print(f"Student {student.names} registered for course {course.name}!")
                    else:
                        print(f"Course {course_name} not found.")
                else:
                    print(f"Student with email {email} not found.")

            elif choice == '4':
                if not grade_book.student_list:
                    print("No students to rank.")
                    continue
                ranking = grade_book.calculate_ranking()
                print("\nRanking of Students based on GPA:")
                for i, student in enumerate(ranking, start=1):
                    gpa = student.GPA if student.GPA is not None else 0.0
                    print(f"{i}. {student.names} - GPA: {student.GPA:.2f}")

            elif choice == '5':
                try:
                    grade = float(input("Enter grade to search for: "))
                    if not (0 <= grade <= 100):
                        raise ValueError("Grade must be between 0 and 100.")
                except ValueError:
                    print("Error: Please enter a valid grade between 0 and 100.")
                    continue
                matching_students = grade_book.search_by_grade(grade)
                if matching_students:
                    print(f"\nStudents with grade {grade}:")
                    for student in matching_students:
                        print(f"- {student.names}")
                else:
                    print(f"No students found with grade {grade}.")

            elif choice == '6':
                email = input("Enter student's email to generate transcript: ")
                student = next((s for s in grade_book.student_list if s.email == email), None)
                if student:
                    transcript = grade_book.generate_transcript(student)
                    print("\nTranscript:")
                    print(transcript)
                else:
                    print(f"Student with email {email} not found.")

            elif choice == '7':
                print("Exiting Grade Book Application.")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 7.")
        
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

