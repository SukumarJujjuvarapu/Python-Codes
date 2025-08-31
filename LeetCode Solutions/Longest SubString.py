def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left, max_len = 0, 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

s=input("Enter a string:")
print(lengthOfLongestSubstring(s))  



##Given a string s, find the length of the longest substring without repeating characters.

