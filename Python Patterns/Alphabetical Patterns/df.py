n=int(input())
stars=n
asc=65
for row in range(1,n+1):
    for st in range(1,stars+1):
        print(chr(asc),end=' ')
        asc+=1
    print()
    stars-=1
