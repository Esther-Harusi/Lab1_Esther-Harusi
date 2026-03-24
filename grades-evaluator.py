#!/usr/bin/env/python3
import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists,
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")

    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    assignments = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    for item in data:
        if item['score'] < 0 or item['score'] > 100:
            print(f"Invalid score in{item['assignment']}: {item['score']}")
            sys.exit(1)
    print("\n--- Processing Grades ---")
  total_weight = sum(item['weight'] for item in data
  formative_weight = sum(item['weight'] for item in data if['group'] == 'Formative')
  summative_weight = sum(item['weight'] for item in data if['group'] == 'Formative')
  if total_weight != 100:
        print(f"Error:Total weight is{total_weight},must be 100")
        sys.exit(1)
  if formative_weight != 60:
        print(f"Error: Formative weight is {formative_weight}, must be 60")
        sys.exit(1)
  if summative_weight != 40:
        print(f"Error:Summative weight is {summative_weight}, must be 40")
        sys.exit(1)
total_grade = 0
   for item in data:
        total_grade = sum([item['score'] * (item['weight'] / 100))
        gpa = (total_grade / 100) * 5.0

        print(f"Final Grade : {total_grade :.2f}%")
        print(f"GPA: {gpa}:.2f}")
    #final grade calculation pass/fail
formative_total = sum(item['score'] * (item['weight'] / 100)
                  for item in data if item['group'] == 'Formative')
summative_total = sum(item['score'] * (item['weight'] / 100)
                  for item in data if item['group'] == 'Summative')
# total percentage of formatives and summatives
formative_percentage = (formative_total / formative_weight) * 100
summative_percentage = (summative_total / summative_weight) * 100

  if formative_percentage >= 50 and summative_percentage >= 50:
        status = "PASSED"
  else:
        status = "FAILED"
    print(f"Formative Average:{formative_percentage:.2f}%")
    print(f"Summative Average: {summative_percentage:.2f}%")
    print(f"Final Marks: {status}")

failed_formatives: = [
     item for item in data
     if item['group'] == 'Formative' and item['score'] < 50
     ]
  if failed_formatives:
        max_weight = max(item['weight'] for item in failed_formatives)
     resubmissions = [
         item['assignment']
         for item in failed_formatives
         if item in failed_formatives
         ]

     print("\nAssignments eligible for resubmission")
     for r in resubmissions:
         print(f"- {r}")
  else:
        print("\nNo resubmissions required")


    # TODO: a) Check if all scores are percentage based (0-100)
    # TODO: b) Validate total weights (Total=100, Summative=40, Formative=60)
    # TODO: c) Calculate the Final Grade and GPA
    # TODO: d) Determine Pass/Fail status (>= 50% in BOTH categories)
    # TODO: e) Check for failed formative assignments (< 50%)
    #          and determine which one(s) have the highest weight for resubmission.
    # TODO: f) Print the final decision (PASSED / FAILED) and resubmission options

    pass

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()

    # 2. Process the features
    evaluate_grades(course_data)
