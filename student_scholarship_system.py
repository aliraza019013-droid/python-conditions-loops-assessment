# Student Scholarship Eligibility System
# This program checks scholarship eligibility using marks, attendance, and family income.

def get_number(prompt, minimum, maximum=None):
    """Get a valid numeric value from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value < minimum or (maximum is not None and value > maximum):
                if maximum is None:
                    print(f"Please enter a value of at least {minimum}.")
                else:
                    print(f"Please enter a value between {minimum} and {maximum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


print("\n=== STUDENT SCHOLARSHIP ELIGIBILITY SYSTEM ===")

# Collect and validate student information.
while True:
    student_name = input("Enter student name: ").strip()
    if student_name:
        break
    print("Name cannot be empty.")

marks = get_number("Enter academic marks (0-100): ", 0, 100)
attendance = get_number("Enter attendance percentage (0-100): ", 0, 100)
family_income = get_number("Enter monthly family income (Rs.): ", 0)

# Check each eligibility condition and record any reasons for ineligibility.
reasons = []

if marks < 80:
    reasons.append("Academic marks are below 80%.")
if attendance < 85:
    reasons.append("Attendance is below 85%.")
if family_income > 50000:
    reasons.append("Monthly family income is above Rs. 50,000.")

# Decide the scholarship category.
if not reasons:
    if marks >= 90:
        scholarship_status = "Eligible"
        scholarship_type = "Full Scholarship"
    else:
        scholarship_status = "Eligible"
        scholarship_type = "Partial Scholarship"
else:
    scholarship_status = "Not Eligible"
    scholarship_type = "No Scholarship"

# Display the complete evaluation report.
print("\n========== SCHOLARSHIP EVALUATION REPORT ==========")
print(f"Student Name: {student_name}")
print(f"Academic Marks: {marks:.2f}%")
print(f"Attendance: {attendance:.2f}%")
print(f"Monthly Family Income: Rs. {family_income:,.2f}")
print(f"Scholarship Status: {scholarship_status}")
print(f"Scholarship Type: {scholarship_type}")

if reasons:
    print("Reasons for Ineligibility:")
    for reason in reasons:
        print(f"- {reason}")

print("===================================================")
