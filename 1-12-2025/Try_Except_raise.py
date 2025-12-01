

def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    return "allowed"

print(check_age(18))
