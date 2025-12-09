#Exercise 1: Write a Python program to create a file named `notes.txt` and write 5 lines of text into it.


# Exercise 1
with open("notes.txt", "w") as file:
    file.write("This is line 1.\n")
    file.write("This is line 2.\n")
    file.write("This is line 3.\n")
    file.write("This is line 4.\n")
    file.write("This is line 5.\n")
print("5 lines written to notes.txt")

#Exercise 2: Write a program to read and print the contents of `notes.txt` line by line


# Exercise 2
with open("notes.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

#Exercise 3: Write a program that appends a new line to an existing file `notes.txt` that says: "This is an appended line."**


with open("notes.txt", "a") as file:
    file.write("This is an appended line.\n")
print("New line appended to notes.txt")
#Exercise 4: Write a program that counts the number of lines in a given file.


with open("notes.txt", "r") as file:
    lines = file.readlines()
    line_count = len(lines)
print(f"Number of lines in notes.txt: {line_count}")

#Exercise 5: Write a program that reads a file and counts the number of words in it.

with open("notes.txt", "r") as file:
    content = file.read()
    words = content.split()
    word_count = len(words)
print(f"Number of words in notes.txt: {word_count}")

#Exercise 6: Write a program to copy the contents of one file (`source.txt`) to another file (`backup.txt`).


with open("source.txt", "r") as source_file:
    content = source_file.read()

with open("backup.txt", "w") as backup_file:
    backup_file.write(content)

print("Contents of source.txt copied to backup.txt")

#exercise 7: Write a program that reads a text file and prints only those lines that contain the word "Python".


# Exercise 7
with open("notes.txt", "r") as file:
    for line in file:
        if "Python" in line:
            print(line.strip())
#Exercise 8: Write a program to read a CSV file named `students.csv` and print the name and marks of each student.**


import csv

# Exercise 8
with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        name = row[0]
        marks = row[1]
        print(f"Name: {name}, Marks: {marks}")


 Exercise 9: Write a program that writes the squares of numbers from 1 to 10 into a file (`numbers.txt`), one per line.


# Exercise 9
with open("numbers.txt", "w") as file:
    for num in range(1, 11):
        file.write(f"{num**2}\n")
print("Squares of numbers from 1 to 10 written to numbers.txt")


### **Exercise 10: Write a log writer program using append mode that adds entries like: "2025-01-01 10:30:45 - Application started". Use the `datetime` module.**

from datetime import datetime

# Exercise 10
def log_entry(message):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("application_log.txt", "a") as log_file:
        log_file.write(f"{current_time} - {message}\n")
    print(f"Log entry added: {current_time} - {message}")

log_entry("Application started")
log_entry("Application stopped")


This will create an `application_log.txt` file with entries like:


2025-01-01 10:30:45 - Application started
2025-01-01 11:00:00 - Application stopped
