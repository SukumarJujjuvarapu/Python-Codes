#WAPTP INDEX POSITIONS OF VOWELS PRESENT IN STRING
s=input()
ip=0
while ip<len(s):
    if s[ip] in "aeiouAEIOU":
        print(ip)
    ip+=1

