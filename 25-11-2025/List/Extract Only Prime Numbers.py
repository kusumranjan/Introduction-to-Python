nums = [10, 11, 12, 13, 17, 20, 23]

prime_nums = []

for num in nums:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:  
            prime_nums.append(num)

print(prime_nums)
