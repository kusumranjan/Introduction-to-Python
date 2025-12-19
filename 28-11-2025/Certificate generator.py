with open("notes.txt", "r") as f:
    students = f.readlines()

for s in students:
    s = s.strip()  # Remove spaces/newlines
    if s:  # Skip empty lines
        certificate_text = f"""
        *********************
        CERTIFICATE OF ACHIEVEMENT
        *********************

        This is to certify that {s} has successfully completed the course.
        """

        file_name = f"certificate_{s.replace(' ', '_')}.txt"
        with open(file_name, "w") as cert_file:
            cert_file.write(certificate_text)

print("Certificates generated successfully!")
