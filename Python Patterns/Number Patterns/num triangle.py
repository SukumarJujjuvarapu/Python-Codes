n=int(input())
stars=1
spaces=n-1
dummy=1
for row in range(1,n+1):
    for spaces in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    spaces-=1
    stars+=1
