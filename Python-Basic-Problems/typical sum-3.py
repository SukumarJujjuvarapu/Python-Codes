#WAPT REPLACE ALL THE VOWELS WITH THEIR INDEX POSITIONS IN THE GIVEN STRING

s=input()
ns=''
for ip in range(len(s)):
    if s[ip] in 'aeiouAEIOU':
                ns+=str(ip)
    else:
        ns+=s[ip]
        
print(ns)
