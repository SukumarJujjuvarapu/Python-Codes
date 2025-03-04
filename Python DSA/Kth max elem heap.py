import heapq

def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]

nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))
print("Kth largest element:", findKthLargest(nums, k))


#Find the k-th largest element in an unsorted array.

