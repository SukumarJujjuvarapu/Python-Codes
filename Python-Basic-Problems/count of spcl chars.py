#WAPTP HOW MANY SPECIAL CHARACTERS IN A GIVEN STRING

s=input()
N=0
for i in s:
    if i.isalpha()==False and i.isdigit()==False:
        N+=1
print(N)
        
