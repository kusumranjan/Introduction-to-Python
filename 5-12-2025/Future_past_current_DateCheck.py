def check_date(s):
    s=datetime.strptime(s, "%Y-%m-%d")
    if date.today() == s.date():
        print("It is todays's date")
    elif date.today() > s.date():
        print("It is Future date")
    else:
        print("It is past date")

check_date("2020-07-31")
