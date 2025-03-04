def climbStairs(n):
    if n <= 2:
        return n
    prev1, prev2 = 2, 1
    for i in range(3, n+1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1

n = int(input("Enter number of steps: "))
print("Ways to climb stairs:", climbStairs(n))

#You can climb a staircase with n steps by taking either 1 step or 2 steps at a time. Find the total number of ways to reach the top.