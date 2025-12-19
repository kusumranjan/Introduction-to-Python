import csv

def export_contacts():
    with open("contacts.csv", "r") as f:
        reader = csv.reader(f)
        next(reader) 
        with open("contacts_export.txt", "w") as out:
            for row in reader:
                name = row[0]
                phone = row[1]
                out.write(f"Name: {name} | Phone: {phone}\n")


export_contacts()
print("contacts_export.txt created successfully!")
