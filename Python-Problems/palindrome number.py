#palindrome number
n=int(input())
dummy=n
rev=0
while dummy>0:
    rem=dummy%10
    rev=rev*10+rem
    dummy//=10   
print(rev)
if n==rev:
    print(n,"is palindrome number")
else:
    print(n,"is not palindrome number")
