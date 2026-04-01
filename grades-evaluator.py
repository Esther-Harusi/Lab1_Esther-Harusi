#!/bin/env/python3
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
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })

        # Handle empty CSV (e.g., after organizer.sh resets it)
        if len(assignments) == 0:
            print("Error: The CSV file is empty. No grades to process.")
            sys.exit(1)

        return assignments

    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)


def evaluate_grades(data):
    """
    Evaluates student grades based on the loaded CSV data.
    """
    print("\n--- Processing Grades ---\n")

    # Validating that all scores are between 0 and 1
    print(">> Step 1: Validating scores...")
    invalid_scores = []
    for item in data:
        if item['score'] < 0 or item['score'] > 100:
            invalid_scores.append(item['assignment'])

    if len(invalid_scores) > 0:
        print(f"  ERROR: The following assignments have invalid scores (must be 0-100):")
        for name in invalid_scores:
            print(f"    - {name}")
        sys.exit(1)
    else:
        print("  All scores are valid (0-100). ✓")


    #  Validate weight
    print("\n>> Step 2: Validating weight...")

    total_weight = 0
    formative_weight = 0
    summative_weight = 0

    for item in data:
        total_weight += item['weight']
        if item['group'] == 'Formative':
            formative_weight += item['weight']
        elif item['group'] == 'Summative':
            summative_weight += item['weight']

    weight_errors = []
    if total_weight != 100:
        weight_errors.append(f"  ERROR: Total weight is {total_weight}, but must equal 100.")
    if formative_weight != 60:
        weight_errors.append(f"  ERROR: Formative weight is {formative_weight}, but must equal 60.")
    if summative_weight != 40:
        weight_errors.append(f"  ERROR: Summative weight is {summative_weight}, but must equal 40.")

    if len(weight_errors) > 0:
        for err in weight_errors:
            print(err)
        sys.exit(1)
    else:
        print(f"  Total weight    : {total_weight}/100 ")
        print(f"  Formative weight: {formative_weight}/60 ")
        print(f"  Summative weight: {summative_weight}/40 ")

    # Calculating weighted grade per group and overall GPA
    
    print("\n>> Step 3: Calculating grades...")

    formative_score   = 0   
    summative_score   = 0   

    for item in data:
        # Contribution = (score / 100) * weight
        contribution = (item['score'] / 100) * item['weight']
        if item['group'] == 'Formative':
            formative_score += contribution
        elif item['group'] == 'Summative':
            summative_score += contribution

    # Converting to percentages for each group

    formative_percentage  = (formative_score / 60) * 100
    summative_percentage  = (summative_score / 40) * 100

    total_grade = formative_score + summative_score   
    gpa = (total_grade / 100) * 5.0

    print(f"  Formative Score : {formative_score:.2f}/60  →  {formative_percentage:.2f}%")
    print(f"  Summative Score : {summative_score:.2f}/40  →  {summative_percentage:.2f}%")
    print(f"  Total Grade     : {total_grade:.2f}/100")
    print(f"  GPA             : {gpa:.2f}/5.0")

    
    # Pass/Fail — student must score >= 50% in BOTH groups
    print("\n>> Step 4: Determining Pass/Fail status...")

    formative_passed  = formative_percentage  >= 50
    summative_passed  = summative_percentage  >= 50
    overall_passed    = formative_passed and summative_passed

    print(f"  Formative  >= 50%: {'PASS ' if formative_passed  else 'FAIL '} ({formative_percentage:.2f}%)")
    print(f"  Summative  >= 50%: {'PASS ' if summative_passed  else 'FAIL '} ({summative_percentage:.2f}%)")


    # Resubmission logic
    failed_formative = []
    for item in data:
        if item['group'] == 'Formative' and item['score'] < 50:
            failed_formative.append(item)

    resubmission_candidates = []
    if len(failed_formative) > 0:
        # Find the highest weight among failed formative assignments
        highest_weight = failed_formative[0]['weight']
        for item in failed_formative:
            if item['weight'] > highest_weight:
                highest_weight = item['weight']

        # Collect all failed formatives that share that highest weight
        for item in failed_formative:
            if item['weight'] == highest_weight:
                resubmission_candidates.append(item)

    
    # Final decision
    print("\n" + "=" * 50)
    print("           FINAL ACADEMIC REPORT")
    print("=" * 50)
    print(f"  GPA             : {gpa:.2f} / 5.0")
    print(f"  Total Grade     : {total_grade:.2f}%")
    print(f"  Formative Grade : {formative_percentage:.2f}%")
    print(f"  Summative Grade : {summative_percentage:.2f}%")
    print("-" * 50)

    if overall_passed:
        print("  FINAL STATUS    : *** PASSED ***")
    else:
        print("  FINAL STATUS    : *** FAILED ***")
        if not formative_passed:
            print(f"    Reason: Formative score ({formative_percentage:.2f}%) is below 50%.")
        if not summative_passed:
            print(f"    Reason: Summative score ({summative_percentage:.2f}%) is below 50%.")

    print("-" * 50)

    if len(resubmission_candidates) > 0:
        print("  RESUBMISSION ELIGIBLE:")
        for item in resubmission_candidates:
            print(f"    → {item['assignment']} "
                  f"(Score: {item['score']}%, Weight: {item['weight']}%)")
    else:
        print("  RESUBMISSION    : No formative assignments eligible for resubmission.")

    print("=" * 50)


if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()

    # 2. Process the features
    evaluate_grades(course_data)

