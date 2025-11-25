

#Exercise 1

max_val = 0
for v in marks.values():
    if v > max_val:
        max_val = v


for k in marks:
    if marks[k] == max_val:
        print(k)
        
        
#Exercise 2

data = {"a": 1, "b": 2, "c": 1}

inverted = {}

for k, v in data.items():
    inverted.setdefault(v, []).append(k)

print(inverted)

#Exercise 3


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged = {}


for d in (dict1, dict2):
    for k, v in d.items():
        if k in merged:
            
            if isinstance(merged[k], list):
                merged[k].append(v)
            else:
                merged[k] = [merged[k], v]
        else:
            merged[k] = v

print(merged)

#Exercise 4

items = {"pen": 50, "book": 120, "bag": 90, "shoes": 250}


filtered = {k: v for k, v in items.items() if v >= 100}

print(filtered)

#Exercise 5


employees = {
    "e1": {"dept": "IT"},
    "e2": {"dept": "HR"},
    "e3": {"dept": "IT"},
}

dept_count = {}

for emp in employees.values():
    dept = emp["dept"]
    dept_count.setdefault(dept, 0)
    dept_count[dept] += 1

print(dept_count)
