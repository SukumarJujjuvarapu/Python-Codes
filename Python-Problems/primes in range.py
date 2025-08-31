start=int(input("enter start:"))
end=int(input("enter end:"))
for n in range(start,end+1):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            print(n,end=" ")

            
