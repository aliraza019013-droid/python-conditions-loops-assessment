"""Student Scholarship Eligibility System.

Evaluates a student's scholarship eligibility from academic marks,
attendance and monthly family income.
"""

import math

# ---- Eligibility rules (constants instead of magic numbers) ----
MIN_MARKS = 80            # minimum academic marks (%) to be eligible
FULL_SCHOLARSHIP_MARKS = 90  # marks (%) at or above which the award is Full
MIN_ATTENDANCE = 85       # minimum attendance (%)
MAX_INCOME = 50000        # maximum monthly family income (Rs.)
PERCENT_MIN, PERCENT_MAX = 0, 100


def read_name(prompt):
    """Ask for a name until a non-empty, letters-and-spaces value is given."""
    while True:
        name = input(prompt).strip()
        if not name:
            print("Error: Name cannot be empty. Please try again.")
        elif not name.replace(" ", "").isalpha():
            print("Error: Name must contain letters and spaces only.")
        else:
            return name


def read_number(prompt, minimum, maximum=None):
    """Ask for a number in [minimum, maximum] until a valid value is given."""
    while True:
        text = input(prompt).strip()
        try:
            value = float(text)
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
        if not math.isfinite(value):
            print("Error: Please enter a valid number.")
        elif value < minimum or (maximum is not None and value > maximum):
            if maximum is None:
                print(f"Error: Value must be at least {minimum}.")
            else:
                print(f"Error: Value must be between {minimum} and {maximum}.")
        else:
            return value


def evaluate_eligibility(marks, attendance, income):
    """Return (eligible, scholarship_type, reasons) for the given values."""
    reasons = []
    if marks < MIN_MARKS:
        reasons.append(f"Academic marks below {MIN_MARKS}% (got {marks:g}%)")
    if attendance < MIN_ATTENDANCE:
        reasons.append(f"Attendance below {MIN_ATTENDANCE}% (got {attendance:g}%)")
    if income > MAX_INCOME:
        reasons.append(f"Monthly family income above Rs. {MAX_INCOME:,} (got Rs. {income:,.0f})")

    if reasons:                                  # at least one rule failed
        return False, "None", reasons
    elif marks >= FULL_SCHOLARSHIP_MARKS:        # all rules met, top marks
        return True, "Full Scholarship", reasons
    else:                                        # all rules met, marks 80 to <90
        return True, "Partial Scholarship", reasons


def display_result(name, eligible, scholarship_type, reasons):
    """Print the final decision."""
    print("\n--- Scholarship Result ---")
    print(f"Student Name: {name}")
    if eligible:
        print("Scholarship Status: Eligible")
        print(f"Scholarship Type: {scholarship_type}")
    else:
        print("Scholarship Status: Not Eligible")
        print("Reason(s):")
        for reason in reasons:
            print(f"  - {reason}")


def main():
    print("=== Student Scholarship Eligibility System ===")
    try:
        name = read_name("Enter student name: ")
        marks = read_number("Enter academic marks (0-100): ", PERCENT_MIN, PERCENT_MAX)
        attendance = read_number("Enter attendance percentage (0-100): ", PERCENT_MIN, PERCENT_MAX)
        income = read_number("Enter monthly family income (Rs.): ", 0)
    except EOFError:
        print("\nError: Input ended before all values were entered.")
        return
    eligible, scholarship_type, reasons = evaluate_eligibility(marks, attendance, income)
    display_result(name, eligible, scholarship_type, reasons)


if __name__ == "__main__":
    main()
