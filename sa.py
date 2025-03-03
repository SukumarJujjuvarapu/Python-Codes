def subarraySum(arr):
    n = len(arr)
    total_sum = 0
    
    # Calculate the sum of all subarrays
    for i in range(n):
        # arr[i] appears in (i+1) * (n-i) subarrays
        total_sum += arr[i] * (i+1) * (n-i)
    
    return total_sum  # This line is now properly indented

# Example usage:
arr = [4, 5, 6]
print (subarraySum(arr))  # In Python 2, use print without parentheses