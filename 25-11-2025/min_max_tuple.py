nums = (33,20,30,60,50)


maximum = nums[0]
minimum = nums[0]

for num in nums:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print("Maximum:", maximum)
print("Minimum:", minimum)
