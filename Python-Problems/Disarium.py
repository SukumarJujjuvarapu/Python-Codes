#WAPT CHECK DISARIUM NUMBER
#135=1^1+3^2+5^3==135
#89=8^1+9^2==89

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
    l-=1
    
if n==summ:
    print(n,"is disarium")
else:
    print(n,"is not disarium")
