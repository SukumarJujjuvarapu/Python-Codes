n=int(input())
dummy=n
summ=0
while dummy>0:
    rem=dummy%10
    summ+=rem
    dummy//=10   
print(summ)
if n%summ==0:
    print(n,"is niven number")
else:
    print(n,"is not niven number")
