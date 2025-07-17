# This is a sample Python script.

import numpy as np
import csv

# Initialize a list to store the grades and scores counter
grades = []
overall_pass_percentage, num_of_failing, num_of_records = 0, 0, 0

failing_dict = {'Exam 1': 0, 'Exam 2': 0, 'Exam 3': 0}
num_of_exams = len(failing_dict)

exam_stats = {
    "mean": [],
    "median": [],
    "std_dev": [],
    "min_score": [],
    "max_score": []
    }
overall_stats = {'mean': 0, 'median': 0, 'std_deviation': 0, 'min_score': 0, 'max_score': 0}

def compute_stats_summary(grades_array, exam_stats, overall_stats):
    exam_stats["mean"] = np.round(np.mean(grades_array, axis=0), 2)
    exam_stats["median"] = np.round(np.median(grades_array, axis=0), 2)
    exam_stats["std_dev"] = np.round(np.std(grades_array, axis=0), 2)
    exam_stats["min_score"] = np.round(np.min(grades_array, axis=0), 2)
    exam_stats["max_score"] = np.round(np.max(grades_array, axis=0), 2)
    overall_stats['mean'] = np.round(np.mean(grades_array), 2)
    overall_stats['median'] = np.round(np.median(grades_array), 2)
    overall_stats['std_deviation'] = np.round(np.std(grades_array), 2)
    overall_stats['min_score'] = np.round(np.min(grades_array), 2)
    overall_stats['max_score'] = np.round(np.max(grades_array), 2)
    return exam_stats, overall_stats


def display_exam_summary(exam_stats):
    print(f"\nSTATISTICS SUMMARY OF THE 3 EXAMS:\n")
    print(f"\tExam 1 Exam 2 Exam 3")
    for key in exam_stats:
        print(f"{key.capitalize()}: {str(exam_stats[key]).strip('[').strip(']')}")

def display_stats_summary(overall_stats):
    print(f"\nOVERALL STATISTICS SUMMARY:\n")
    for key in overall_stats:
        print(f"{key.capitalize()}: {str(overall_stats[key]).strip('[').strip(']')}")
    
def display_summary(num_of_records, failing_dict):
    print()
    for key in failing_dict:
        print(f"There are {failing_dict[key]} students out of {num_of_records} is/are failing {key}.")


def compute_passing_percentage(num_of_records, num_of_failing, num_of_exams):
    total_of_exams = num_of_records * num_of_exams
    total_of_passing = total_of_exams - num_of_failing
    return round((total_of_passing/total_of_exams) * 100, 2)

# Open and read the CSV file
with open('grades.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    hearder = next(reader) # Skip the header row
    num_of_passing = 0
    
    for row in reader:
        # Extract score1, score2, score3 (assumed to be at indices 2, 3, 4
        grades.append([float(row[2]), float(row[3]), float(row[4])])
        
        if float(row[2]) < 60:
            failing_dict['Exam 1'] += 1
            num_of_failing += 1
        if float(row[3]) < 60:
            failing_dict['Exam 2'] += 1
            num_of_failing += 1
        if float(row[4]) < 60:
            failing_dict['Exam 3'] += 1
            num_of_failing += 1
        num_of_records += 1
    
# Convert the list of scores to a Numpy array
grades_array = np.array(grades)


if __name__ == '__main__':
     compute_stats_summary(grades_array, exam_stats, overall_stats)
     display_exam_summary(exam_stats)
     display_stats_summary(overall_stats)
     display_summary(num_of_records, failing_dict)
     overall_pass_percentage = compute_passing_percentage(num_of_records, num_of_failing, num_of_exams)
     print(f"\nThe overall pass percentage across all exams are: {overall_pass_percentage} %.")
