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
        print("3. Register Student for Course")
        print("4. Assign Grade to Course")
        print("5. Calculate Ranking")
        print("6. Search by Grade")
        print("7. Generate Transcript")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        try:
            if choice == '1':
                email = input("Enter student's email: ")
                names = input("Enter student's names: ")
                student = Student(email, names)
                grade_book.add_student(student)
                print("Student added successfully!")

            elif choice == '2':
                name = input("Enter course name: ")
                trimester = input("Enter trimester: ")
                credits = int(input("Enter credits: "))
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
                email = input("Enter student's email: ")
                course_name = input("Enter course name: ")
                grade = float(input("Enter grade: "))

                student = next((s for s in grade_book.student_list if s.email == email), None)
                if student:
                    try:
                        student.assign_grade(course_name, grade)
                        print(f"Grade {grade} assigned to course {course_name} for student {student.names}.")
                    except ValueError as e:
                        print(f"Error: {e}")
                else:
                    print(f"Student with email {email} not found.")

            elif choice == '5':
                ranking = grade_book.calculate_ranking()
                print("\nRanking of Students based on GPA:")
                for i, student in enumerate(ranking, start=1):
                    print(f"{i}. {student.names} - GPA: {student.GPA:.2f}")

            elif choice == '6':
                grade = float(input("Enter grade to search for: "))
                matching_students = grade_book.search_by_grade(grade)
                if matching_students:
                    print(f"\nStudents with grade {grade}:")
                    for student in matching_students:
                        print(f"- {student.names}")
                else:
                    print(f"No students found with grade {grade}.")

            elif choice == '7':
                email = input("Enter student's email to generate transcript: ")
                student = next((s for s in grade_book.student_list if s.email == email), None)
                if student:
                    transcript = grade_book.generate_transcript(student)
                    print("\nTranscript:")
                    print(transcript)
                else:
                    print(f"Student with email {email} not found.")

            elif choice == '8':
                print("Exiting Grade Book Application.")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 8.")
        
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
