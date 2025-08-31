#WAPTP EVEN NUMBER WITHIN A GIVEN RANGE

LL=int(input())
UL=int(input())
for i in range(LL,UL+1):
    if i%2==0:
        print(i)
