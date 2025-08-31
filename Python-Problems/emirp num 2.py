n=int(input("Enter a number: "))
reverse=int(str(n)[::-1])
def isPrime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
        
if isPrime(n) and isPrime(reverse) and n!=reverse:
    print('emirp number')
else:
    print('not emirp number')
