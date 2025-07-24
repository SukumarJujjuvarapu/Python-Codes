#WAPTP HOW MANY VOWELS PRESENT IN A GIVEN STRING

s=input()
v="AEIOUaeiou"
c=0         
for ele in s:
    if ele in v:
        c+=1
print(c)


'''taking string input from user'''
'''assuming tha there are no vowels initially and taking count c as variable'''
'''for loop starts
s=ashu
iteration 1
ele=a
a is in v
c=1
ele=s
s not in v
c=1
ele=s
h not in v
c=1
ele=s
u in v
c=2
'''
