def write_report(name,amount):
    report=f"""
    Product Report
    Product_name={name}
    Product_amount={amount}

"""
    with open("record.txt", "w") as f:
        f.write(report)



write_report("Shampoo",234)
