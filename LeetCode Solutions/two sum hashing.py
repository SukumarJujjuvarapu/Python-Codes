def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        if target - num in num_map:
            return [num_map[target - num], i]
        num_map[num] = i
    return []

nums = list(map(int, input("Enter array elements separated by space: ").split()))
target = int(input("Enter target sum: "))
print("Indices of Two Numbers:", twoSum(nums, target))


##Given an array nums and an integer target, return indices of the two numbers that add up to target.


