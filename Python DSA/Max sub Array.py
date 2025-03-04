def maxSubarraySum(arr, k):
    max_sum, curr_sum = 0, sum(arr[:k])
    for i in range(k, len(arr)):
        curr_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, curr_sum)
    return max_sum
arr = list(map(int, input("Enter array elements separated by space: ").split()))
k = int(input("Enter the size of the subarray: "))
print("Maximum Sum of Subarray of Size", k, ":", maxSubarraySum(arr, k))



##Given an array of integers and an integer k, find the maximum sum of any contiguous subarray of size k.

