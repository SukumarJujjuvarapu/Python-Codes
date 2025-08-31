n=int(input())
if n>1:
    divisor=2
    while divisor<n//2+1:
        if n%divisor==0:
            print("n is not prime number")
            break
        divisor+=1
    else:
        print("n is prime number")
else:
    print("n is not prime number")
