#finding sum of even index positions of all even nums present in string
#approach 1
s=input()
sm=0
ip=0
while ip<len(s):
    if ip%2==0:
        if s[ip].isdigit():
            if int(s[ip])%2==0:
                sm+=ip
    ip+=1
print(sm)

