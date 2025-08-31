a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
if a>b and a>c:
    if a>d and a>e:
        print("a is max")
if b>c and b>d:
    if b>e:
        print("b is max")
if c>d and c>e:
    print("c is max")
if d>e:
    print("d is max")
else:
    print("e is max")
