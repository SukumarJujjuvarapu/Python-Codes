def rob(nums):
    prev1, prev2 = 0, 0
    for num in nums:
        prev1, prev2 = max(prev2 + num, prev1), prev1
    return prev1

nums = list(map(int, input("Enter house money values: ").split()))
print("Maximum money that can be robbed:", rob(nums))
 ##You are a robber, and you cannot steal from two adjacent houses. Find the maximum money you can steal.
 # Solution (O(N) DP)