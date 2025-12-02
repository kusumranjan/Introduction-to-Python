#Write to JSON file

df.to_json("Student.json", orient="records",indent=4)

print("JSON file created successfully")
