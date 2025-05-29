# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# Change Log: (Who, When, What)
# Yunjia He,5/28/2025,Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = """---- Course Registration Program ----
  Select from the following menu:
    1. Register a Student for a Course
    2. Show current data
    3. Save data to a file
    4. Exit the program
-----------------------------------------
"""
FILE_NAME: str = "Enrollments.json"


# Define the Data Variables
menu_choice: str = ""
students: list = []

class FileProcessor:

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """Reads data from a JSON file into a list of dictionaries"""
        global students
        file = file_name
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("The file was not found.", e)
            quit()
        except Exception as e:
            IO.output_error_messages("Error!",e)
        finally:
            if file and not file.close:
                file.close()
        students = student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """Writes data from a list of dictionaries to a JSON file"""
        file = file_name
        try:
            file = open(file_name, "w")
            json.dump(student_data, file, indent=2)
            file.close()
            print("Data saved! The current data is:")
        except FileNotFoundError as e:
            IO.output_error_messages("The file was not found!", e)
        except Exception as e:
            IO.output_error_messages("Error!",e)
        finally:
            if file and not file.close:
                file.close()

        for student in students:
            print(f'{student["First_name"]},'
                  f'{student["Last_name"]}, '
                  f'{student["Course"]}')
        print()

class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    Yunjia,5/28/2025,Created Class
    Yunjia,5/28/2025,Added a function to display error messages
    Yunjia,5/28/2025,Added a function to display menu
    Yunjia,5/28/2025,Added a function to input menu choice
    Yunjia,5/28/2025,Added a function to display current data
    Yunjia,5/28/2025,Added a function to input student data
    """
    @staticmethod
    def output_error_messages(message:str, error: Exception = None):
        """Print error messages."""
        print(f"Error message:{message}")
        print(error)

    @staticmethod
    def output_menu():
        """Print menu."""
        print(MENU)

    @staticmethod
    def input_menu_choice():
        """Prompts the user to enter choice"""
        global menu_choice
        menu_choice = input("What would you like to do? ")
        print()

    @staticmethod
    def output_student_courses(student_data: list):
        """print current students with courses"""
        print("The current data is:")
        for student in student_data:
            print(f'{student["First_name"]}, '
                  f'{student["Last_name"]}, '
                  f'{student["Course"]}')
        print()

    @staticmethod
    def input_student_data(student_data: list):
        """
        Prompts the user to enter their first name, last name and course name.
        Validates that names contain only letters.
        """
        student_first_name:str = ""
        student_last_name:str = ""
        try:
            student_first_name = input("Enter the student's first name? ")
            student_last_name = input("Enter the student's last name? ")

            if not student_first_name.isalpha():
                raise ValueError("First name should not contain numbers!")
        except Exception as e:
            IO.output_error_messages("Error!",e)

        try:
            if not student_last_name.isalpha():
                raise ValueError("Last name should not contain numbers!")
        except Exception as e:
            IO.output_error_messages("Error!",e)

        course_name = input("Please enter the course's name? ")
        student_data.append({
            "First_name": student_first_name,
            "Last_name": student_last_name,
            "Course": course_name
        })
        print()

FileProcessor.read_data_from_file(FILE_NAME, students)

while True:
    IO.output_menu()

    IO.input_menu_choice()

    if menu_choice == "1":
        IO.input_student_data(students)
    elif menu_choice == "2":
        IO.output_student_courses(students)
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)
    elif menu_choice == "4":
        break
    else:
        print("Please only choose option 1~4")
        print()
print("Program Ended")