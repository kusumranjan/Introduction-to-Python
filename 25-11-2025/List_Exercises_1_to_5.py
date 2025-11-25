#exercise 1


nums = [10, -3, 5, -8, 7, -1]

result = []


for num in nums:
    if num < 0:
        result += [num]


for num in nums:
    if num >= 0:
        result += [num]

print(result)

#exercise 2

nums = [1, 2, 3, 2, 4, 1, 5, 1]

unique_nums = []

for num in nums:
    if num not in unique_nums:
        unique_nums += [num]

print(unique_nums)


#exercise 3


nums = [1, 2, 3, 4, 5]
N = 2

for i in range(N):
    first = nums[0]

    for j in range(len(nums)-1):
        nums[j] = nums[j+1]
    nums[-1] = first
print(nums)

#exercise 4


words = ["hi", "cat", "a", "dog", "go", "apple"]

result = []

for word in words:
    if len(word) >= 3:
        result += [word]

print(result)

#exercise 5

nested_list = [[1, 2], [3, 4], [5]]
flat_list = []

for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)

print(flat_list)
