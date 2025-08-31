n=int(input())
if n>1:
    for i in range(2,n//2+1):
        if n%i==0:
            print("not prime")
            break
    else:
        print("is prime")
else:
    print("not prime")
            
