#WAPTP HOW MANY TIMES A SUB-STRING PRESENT IN A MAIN STRING

MS=input()
SS=input()
c=0
for ip in range(len(MS)-len(SS)+1):
    if MS[ip:ip+len(SS):]==SS:
        c+=1
print(c)
