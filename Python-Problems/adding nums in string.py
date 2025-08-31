#WAPT ADD NUMBERS IN A STRING
st=input()
s=0
for ele in st:
    if ele.isdigit():
        s+=int(ele)
print(s)
        
