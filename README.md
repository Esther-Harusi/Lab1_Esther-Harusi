1.  Grades-evaluator.py reads the student's grades from a CSV file, validates the data, calculates the  GPA, and determines if a student has failed or passed. It also identifies assignments that are eligible for resubmission. 2. The organizer.sh archives the current grades.csv with a timestamp, resets the workspace, and logs each activity.

**Project Structure**

lab1/
├── grade-evaluator.py    
├── organizer.sh         
├── grades.csv         
├── README.md             
└── archive/             


**Running grade-evaluator.py**
On my  terminal I navigated to the project folder:
cd /lab1
Running  the script:
python3 grade-evaluator.py
 I get prompted to enter the CSV filename when prompted:
grades.csv
The program will then:
Validate scores and weights
Calculate total grade and GPA
Determine Pass/Fail status
List assignments eligible for resubmission

**Running organizer.sh**
Making  the script executable :
chmod +x organizer.sh
Running  the script:
./organizer.sh
The script will:
Create archive/ if it does not exist
Move grades.csv to archives with a timestamp
A  new empty grades.csv is created automatically
The activity is then logged  in the organizer.log

View the log:

cat organizer.log
GPA Formula
GPA = (Total Grade / 100) × 5.0

Pass requires ≥50% in both Formative and Summative categories independently.

**Error Handling**
| Scenario | Program Response |
|----------|-----------------|
| grades.csv not found | Displays an error message and exits |
| CSV file is empty | Displays an error message and exits |
| Score outside 0–100 | Lists invalid assignments and exits |
| Incorrect total weight | Displays weight validation error and exits |
| Incorrect Formative/Summative weights | Displays category weight errors and exits |
