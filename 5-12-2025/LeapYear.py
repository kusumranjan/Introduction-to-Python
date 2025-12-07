import _strptime
from time import strftime

def check(year):
    if year%4==0:
        print("Leap year")
    else:
        print("Not leap year")


check(2020)
check(2021)
