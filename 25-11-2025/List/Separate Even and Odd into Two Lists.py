
nums = [10, 3, 5, 12, 8, 7, 1]

even = []
odd = []

for num in nums:
    if num % 2 == 0:   
        even = even + [num]  
    else:              
        odd = odd + [num]    

print("Even:", even)
print("Odd:", odd)
