s=input("enter a string")

def check_vowel(s):
    w=" "
    for c in s.lower():
        if c in "aeiou":
            continue
        else:
            w+=c
    return w
print(check_vowel(s))
