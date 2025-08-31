# WRITING  A CODE BASED ON THE INPUT GIVEN BELOW

L=eval(input())
s=0
for i in L:
    if isinstance(i,int):
        s+=i
    elif isinstance(i,str) and i.isdigit():
        s+=int(i)
print(s)
