n=int(input())
stars=1
asc=65
for row in range(1,n+1):
    for st in range(1,n+1):
        print(chr(asc),end=' ')
    print()
    asc+=1
    if row<n//2+1:
        asc+=1
    else:
        asc-=1
    
