def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

s = input("Enter a string containing only brackets: ")
print("Is valid parentheses:", isValid(s))


##Given a string s containing ()[]{}, determine if the string is valid. A valid string must follow these rules:
#Open brackets must be closed by the same type of bracket.
#Open brackets must be closed in the correct order.7