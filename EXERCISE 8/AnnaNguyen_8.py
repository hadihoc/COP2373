# This program collects students' first name and last name and their
# three exam scores.  Write these data in the .csv file and then display
# these summary on the console.

import csv
import os
import re


# Check if the grades.csv file exists
def is_file_exists(filename):
    if os.path.isfile(filename):
        return True
    else:
        return False


# Write header to the file
def write_header(filename, student_data):
    with open(filename, 'w', newline="") as file:
        fieldnames = list(student_data[0].keys())  # Convert keys to list
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(student_data)

# Collect students data: first name, last name, and the 3 exam scores
def collect_student_data(student_data, num_students):
    for j in range(num_students):
        student_info = {}

        student_info['First Name'] = input(f"\nEnter student #{j + 1} first name: ")
        student_info['Last Name'] = input("Enter last name: ")

        for i in range(1, 4):  # Exams 1 to 3
            while True:
                score = input(f"Enter Exam {i} score: ")
                if score.isdigit():
                    student_info[f"Exam {i}"] = int(score)
                    break
                else:
                    print("Invalid input. Please enter a numeric score.")

        student_data.append(student_info)

# Write student data into .csv file
def write_data(filename, student_data):
    with open(filename, 'a', newline="") as file:
        fieldnames = list(student_data[0].keys())
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerows(student_data)


# Print a list of student names and their exam scores
def print_summary(filename):
    is_header = False

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for word in row:
                if " " not in word:
                    print(format(word, '15'), end=" ")
                else:
                    print(format(word, '16'), end="")
                    is_header = True
            if is_header:
                print()
                print('{:<16}'.format('*' * 10), end="")
                print('{:<16}'.format('*' * 9), end="")
                print('{:<16}'.format('*' * 6), end="")
                print('{:<16}'.format('*' * 6), end="")
                print('*' * 6)
                is_header = False
            print()
# +++++++++++++++++++++++++++++++++++++++++++++++++

def main():
    student_data = []
    filename = 'grades.csv'
    num_students = 0

    # Ask how many students to enter
    while True:
        num_of_students = input("Enter the number of students: ")
        if num_of_students.isdigit():
            num_students = int(num_of_students)
            break
        else:
            print("You've entered an invalid number.")

    collect_student_data(student_data, num_students)

    if is_file_exists(filename):
        if not student_data:
            print("student_data list is empty.")
        else:
            write_data(filename, student_data)
    else:
        if not student_data:
            print("student_data list is empty.")
        else:
            write_header(filename, student_data)
    print()
    print_summary(filename)


# *******************************************************

if __name__ == "__main__":
    main()






    
            
    
    
