# PROGRAM FOR ARMSTRONG NUMBER

# 371  no of digits are 3
# 371= 3^3+ 7^3+ 1^3 ==371

#1634  no of digits are 4
#1634= 1^4+ 6^4+ 3^4+ 4^4==1634

#APPROACH-1

n=int(input())
dummy1=n
dummy2=n
summ=0
l=0
while dummy1>0:
    dummy1//=10
    l+=1
while dummy2>0:
    rem=dummy2%10
    dummy2//=10
    summ+=rem**l
if n==summ:
    print(n,"is ARMSTRONG")
else:
    print(n,"is NOT ARMSTRONG")


#APPROACH-2

    
'''n=int(input())
dummy1=n
dummy2=n
summ=0
l=len(str(n))
while dummy2>0:
    rem=dummy2%10
    dummy2//=10
    summ+=rem**l
if n==summ:
    print(n,"is ARMSTRONG")
else:
    print(n,"is NOT ARMSTRONG")'''
    
