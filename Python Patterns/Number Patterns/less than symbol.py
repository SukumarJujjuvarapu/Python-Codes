n=int(input())
stars=1
spaces=n//2
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print('  ',end='  ')
    for st in range(1,stars+1):
        print(dummy,end='  ')
    print()
    dummy+=1
    if row<n//2+1:
        spaces-=1
    else:
        spaces+=1
