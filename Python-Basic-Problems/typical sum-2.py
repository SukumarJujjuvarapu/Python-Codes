#WAPTP SUM OF EVEN INDEX POSITIONS OF ALL THE EVEN NUMBERS PRESENT IN A STRING

s=input()
sum=0
for ip in range(len(s)):
    if ip%2==0:
        if s[ip].isdigit():
            if int(s[ip])%2==0:
                sum+=ip
print(sum)


#APPROACH - 2
'''s=input()
sum=0
for ip in range(0,len(s),2):
        if s[ip].isdigit():
            if int(s[ip])%2==0:
                sum+=ip
print(sum)'''


