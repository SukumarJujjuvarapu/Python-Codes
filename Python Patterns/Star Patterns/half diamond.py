n=int(input())
stars=1
for row in range(1,n+1):
    for st in range(1,stars+1):
        print('*',end=" ")
    print()
    if row<n//2+1:
        stars+=1
    else:
        stars-=1
