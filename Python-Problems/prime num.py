n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        print(i)
        c+=1
print("count = ",c)
if c==2:
    print(n,"is prime")
else:
    print(n,"is not prime")
