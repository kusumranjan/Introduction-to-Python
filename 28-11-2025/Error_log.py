with open("catalogs.txt", "r") as r:
    f = r.readlines()

e = 0
w = 0
info = 0 

for line in f:
    if "ERROR" in line:
        e += 1
    elif "WARNING" in line:
        w += 1
    elif "INFO" in line:
        info += 1

with open("log.txt", "w") as out:  # FIX: use write mode
    out.write(f"ERROR: {e}\n")
    out.write(f"WARNING: {w}\n")
    out.write(f"INFO: {info}\n")

print("Log summary generated successfully!")
