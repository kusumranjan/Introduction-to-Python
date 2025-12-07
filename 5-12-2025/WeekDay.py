def week_cal(start,end):
    start=datetime.strptime(start,"%Y-%m-%d")
    end=datetime.strptime(end,"%Y-%m-%d")
    e=end-start
    e=e.days

    f=e//7

    g=e%7

    w=f*5+g
    print(w)



week_cal("2025-10-12","2025-12-12")
