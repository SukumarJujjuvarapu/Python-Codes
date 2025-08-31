n=int(input())
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(dummy,end=' ')
        if row%2==0:
            dummy+=2
        else:
            dummy+=1
    print()
