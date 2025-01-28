nums = [4, 12, 9, 18, 7, 20]
res = []

def greather10(nums):
    for num in nums:
        if(num % 2 == 0):
            if(num >= 10):
                res.append(num)
    return res

print(greather10(nums))