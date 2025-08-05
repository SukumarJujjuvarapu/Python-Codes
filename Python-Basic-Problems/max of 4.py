a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a>b and a>c:
    if a>d:
        print("a is max")
if b>c and b>d:
    print("b is max")
if c>d:
    print("c is max")
else:
    print("d is max")
