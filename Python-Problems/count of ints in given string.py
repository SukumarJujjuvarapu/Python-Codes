#WAPTP HOW MANY INTEGERS IN A GIVEN STRING

s=input()
sum=0
for i in s:
    if i.isdigit():
        sum+=1
print(sum)
        

