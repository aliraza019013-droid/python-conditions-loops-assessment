# Python Conditions & Loops Assessment

## Project Overview

This repository contains two beginner-friendly Python applications developed for a programming assessment. The applications demonstrate conditional statements, loops, input validation, arithmetic, counters, and accumulators through practical examples.

## Task 1: Student Scholarship Eligibility System

This program evaluates a student's eligibility for a university scholarship using academic marks, attendance, and monthly family income.

### Eligibility Criteria
- Academic marks must be at least 80%.
- Attendance must be at least 85%.
- Monthly family income must be Rs. 50,000 or less.
- Students meeting all criteria with marks of 90% or above receive a Full Scholarship.
- Students meeting all criteria with marks from 80% to below 90% receive a Partial Scholarship.
- Students who fail any condition are shown as Not Eligible, with the reason(s).

### Concepts Used
- Variables and data types
- `input()` and `print()`
- `if`, `elif`, and `else` statements
- Comparison and logical operators
- Input validation
- Functions and string formatting

### Run the Program
```bash
python student_scholarship_system.py
```

### Sample Input
```text
Enter student name: Ali
Enter academic marks (0-100): 92
Enter attendance percentage (0-100): 90
Enter monthly family income (Rs.): 40000
```

### Sample Result
```text
Scholarship Status: Eligible
Scholarship Type: Full Scholarship
```

## Task 2: Smart Pharmacy Inventory & Sales Management System

This program processes multiple medicines, checks stock availability, calculates sales, updates remaining stock, and produces a daily revenue summary.

### Main Features
- Processes the number of medicines entered by the user.
- Collects medicine name, available stock, unit price, and quantity sold.
- Completes a sale only if enough stock is available.
- Calculates sales amount and remaining stock.
- Displays a warning when remaining stock is below 10 units.
- Uses an accumulator for total revenue.
- Uses counters for processed medicines and medicines requiring restocking.
- Displays a final pharmacy report.

### Concepts Used
- Variables and data types
- `input()` and `print()`
- `for` loop and `range()`
- Conditional statements
- Arithmetic operators
- Counters and accumulators
- Input validation
- Functions and string formatting

### Run the Program
```bash
python pharmacy_inventory_system.py
```

### Sample Input
```text
How many different medicines do you want to process? 2

Medicine 1:
Medicine name: Panadol
Available stock: 50
Price per unit: 20
Quantity sold: 15

Medicine 2:
Medicine name: Brufen
Available stock: 8
Price per unit: 30
Quantity sold: 5
```

### Sample Result
```text
Medicine: Panadol
Total Sales: Rs. 300.00
Remaining Stock: 35

Medicine: Brufen
Total Sales: Rs. 150.00
Remaining Stock: 3
WARNING: Low stock! Restocking required.

Total Medicines Processed: 2
Total Pharmacy Revenue: Rs. 450.00
Medicines Requiring Restocking: 1
```

## Project Structure

```text
python-conditions-loops-assessment/
├── student_scholarship_system.py
├── pharmacy_inventory_system.py
└── README.md
```

## Requirements

- Python 3.x
- Visual Studio Code or another Python editor (recommended)
- No external libraries are required

## How to Use

1. Download or clone this repository.
2. Open the project folder in your code editor.
3. Open a terminal in the project folder.
4. Run either Python file using the commands above.
5. Enter the requested information and review the report.

## Conclusion

The Student Scholarship Eligibility System demonstrates decision-making with conditional statements. The Smart Pharmacy Inventory & Sales Management System demonstrates repetition with `for` loops, conditions inside loops, counters, and accumulators. Together, these programs show how basic Python concepts can be applied to practical problems.

**Project Name:** Python Conditions & Loops Assessment  
**Language:** Python 3  
**Repository Name:** `python-conditions-loops-assessment`
