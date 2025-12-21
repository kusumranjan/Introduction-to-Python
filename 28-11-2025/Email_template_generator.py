with open("notex.txt", "r") as f:
    names = f.readlines()

def email_sender(name):
    email_text = f"""
Dear {name.strip()},
Your Training Starts Tomorrow!
Regards,
Training Team
"""
    filename = input("enter file name")

    with open(filename, "w") as f:
        f.write(email_text)

for name in names:
    email_sender(name)

print("Email templates generated successfully!")
