#WAPTP SUM of all INDEX POSITIONS OF ALL CONSONANATS PRESENT IN A GIVEN STRING
s=input()
sm=0
ip=0
while ip<len(s):
    if s[ip].isalpha():
        if s[ip] not in "AEIOUaeiou":
            sm+=ip
    ip+=1
print(sm)



#WAPTP SUM of all INDEX POSITIONS OF ALL vowels PRESENT IN A GIVEN STRING
'''s=input()
sm=0
ip=0
while ip<len(s):
    if s[ip].isalpha():
        if s[ip]  in "AEIOUaeiou":
            sm+=ip
    ip+=1
print(sm)'''
