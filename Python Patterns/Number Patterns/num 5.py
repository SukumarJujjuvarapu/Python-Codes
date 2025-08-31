n=int(input())
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=n
    print()
