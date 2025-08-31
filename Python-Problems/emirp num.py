n=int(input("Enter a number: "))
reverse=int(str(n)[::-1])
if n!=reverse:
    for i in range(2,n//2+1):
        if n%i==0:
            print('Not EMIRP Number')
            break
    else:
        for j in range(2,n//2+1):
            if n%j==0:
                print('Not EMIRP Number')
                break
        else:
            print('EMIRP Number')
else:
    print('Not EMIRP Number')
