s=input()
c=0
for ele in s:
    if not ele.isalnum():
        c+=1
print(c)
