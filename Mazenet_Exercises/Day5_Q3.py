 1. **Student Certificate Batch Generator**

Write a program that reads a list of student names from `students.txt` and generates a certificate file for each student automatically.

```python
# Read student names from the file
with open("students.txt", "r") as file:
    students = file.readlines()

# Generate a certificate for each student
for student in students:
    student = student.strip()  # Remove any leading/trailing whitespace
    certificate_content = f"Certificate of Completion\n\nThis is to certify that {student} has successfully completed the course.\n\nDate: 2025\n"
    
    # Save each certificate in a separate file
    with open(f"{student}_certificate.txt", "w") as cert_file:
        cert_file.write(certificate_content)
    
    print(f"Certificate generated for {student}")
```

---

### 2. **Expense Report Generator**

Create a function that accepts multiple expense items (name, amount) and writes a formatted expense report into `report.txt`.

```python
def generate_expense_report(expenses):
    with open("report.txt", "w") as file:
        file.write("Expense Report\n")
        file.write("--------------\n")
        total = 0
        for item, amount in expenses:
            file.write(f"{item}: ${amount}\n")
            total += amount
        file.write(f"\nTotal: ${total}")

# Example usage:
expenses = [("Lunch", 15), ("Taxi", 30), ("Hotel", 120)]
generate_expense_report(expenses)
```

---

### 3. **Attendance Log Writer**

For each student name given by the user, append an entry to `attendance.log` with timestamp and status (Present/Absent).

```python
import datetime

def log_attendance(student_name, status):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("attendance.log", "a") as file:
        file.write(f"{timestamp} - {student_name}: {status}\n")

# Example usage:
log_attendance("John Doe", "Present")
log_attendance("Jane Smith", "Absent")
```

---

### 4. **Invoice Generator from CSV**

Read a CSV file `orders.csv` containing columns: item, quantity, price. Generate an invoice file that lists all items and the final total.

```python
import csv

def generate_invoice(csv_file, output_file):
    total = 0
    with open(csv_file, newline="") as file:
        reader = csv.reader(file)
        with open(output_file, "w") as invoice:
            invoice.write("Item\tQuantity\tPrice\tTotal\n")
            for row in reader:
                item, quantity, price = row[0], int(row[1]), float(row[2])
                item_total = quantity * price
                invoice.write(f"{item}\t{quantity}\t{price}\t{item_total}\n")
                total += item_total
            invoice.write(f"\nTotal: {total}")

# Example usage:
generate_invoice("orders.csv", "invoice.txt")
```

---

### 5. **Automated Welcome Letter Creator**

Write a function that takes a student's name and course, and generates a personalized welcome letter in a text file.

```python
def create_welcome_letter(student_name, course):
    letter_content = f"Dear {student_name},\n\nWelcome to the {course} course. We are excited to have you!\n\nBest regards,\nCourse Team"
    
    with open(f"{student_name}_welcome_letter.txt", "w") as file:
        file.write(letter_content)

# Example usage:
create_welcome_letter("John Doe", "Python Programming")
```

---

### 6. **Error Log Application**

Build a function `log_error(message)` that writes errors into `error.log` with timestamps. Simulate errors by calling the function 5 times.

```python
import datetime

def log_error(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("error.log", "a") as file:
        file.write(f"{timestamp} - ERROR: {message}\n")

# Simulating errors
for _ in range(5):
    log_error("An error occurred in the system.")
```

---

### 7. **Product Catalog Formatter**

Read a text file `products.txt` with product names and prices. Generate a formatted catalog file `catalog.txt` with alignment.

```python
def format_product_catalog(input_file, output_file):
    with open(input_file, "r") as file:
        products = file.readlines()
    
    with open(output_file, "w") as file:
        file.write(f"{'Product':<20} {'Price':<10}\n")
        file.write("="*30 + "\n")
        for product in products:
            name, price = product.strip().split(',')
            file.write(f"{name:<20} {price:<10}\n")

# Example usage:
format_product_catalog("products.txt", "catalog.txt")
```

---

### 8. **Quiz File Generator**

Write a function that takes a list of questions and writes them into `quiz.txt` with question numbers. Include blank lines for answers.

```python
def generate_quiz(questions):
    with open("quiz.txt", "w") as file:
        for idx, question in enumerate(questions, start=1):
            file.write(f"Q{idx}. {question}\n")
            file.write("Answer: \n\n")

# Example usage:
questions = ["What is your name?", "What is the capital of France?", "What is 2 + 2?"]
generate_quiz(questions)
```

---

### 9. **Order Summary From User Input**

Ask the user for item name, quantity, and price for 3 items. Then generate a summary file `order_summary.txt` with totals.

```python
def generate_order_summary():
    total = 0
    with open("order_summary.txt", "w") as file:
        file.write("Order Summary\n")
        file.write("--------------\n")
        for i in range(3):
            item = input(f"Enter item {i+1} name: ")
            quantity = int(input(f"Enter quantity for {item}: "))
            price = float(input(f"Enter price for {item}: "))
            item_total = quantity * price
            file.write(f"{item}: {quantity} x {price} = {item_total}\n")
            total += item_total
        file.write(f"\nTotal: {total}")

# Example usage:
generate_order_summary()
```

---

### 10. **System Log Analyzer**

Read `system.log` and count:

* Number of ERROR lines
* Number of WARNING lines
* Number of INFO lines
  Write the summary into `log_summary.txt`.

```python
def analyze_system_log():
    error_count = warning_count = info_count = 0
    
    with open("system.log", "r") as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1
            elif "INFO" in line:
                info_count += 1
    
    with open("log_summary.txt", "w") as file:
        file.write(f"ERROR: {error_count}\n")
        file.write(f"WARNING: {warning_count}\n")
        file.write(f"INFO: {info_count}\n")

# Example usage:
analyze_system_log()
```

---

### 11. **Email Template Generator**

Write a script that reads names from `names.txt` and generates email templates like:

```
Dear <name>,
Your training session starts tomorrow.
Regards,
Training Team
```

Each email should be saved into separate files.

```python
def generate_email_templates():
    with open("names.txt", "r") as file:
        names = file.readlines()

    for name in names:
        name = name.strip()
        email_content = f"Dear {name},\n\nYour training session starts tomorrow.\n\nRegards,\nTraining Team"
        
        with open(f"{name}_email.txt", "w") as email_file:
            email_file.write(email_content)

# Example usage:
generate_email_templates()
```

---

### 12. **Contact Exporter**

Read a CSV file `contacts.csv` with name and phone columns. Generate a formatted text file `contacts_export.txt` listing:

```
Name: Rahul  | Phone: 9988776655
Name: Aisha  | Phone: 9123456789
```

```python
import csv

def export_contacts():
    with open("contacts.csv", newline="") as file:
        reader = csv.reader(file)
        with open("contacts_export.txt", "w") as output_file:
            for row in reader:
                name, phone = row
                output_file.write(f"Name: {name}  | Phone: {phone}\n")

