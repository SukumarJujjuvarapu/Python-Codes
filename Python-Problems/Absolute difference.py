#WAPTP ABSOLUTE DIFFERENCE
l=eval(input())
os=0
es=0
for i in l:
    if i%2==0:
        es+=i
    else:
        os+=i
if es>os:
    print(es-os)
else:
    print(os-es)


'''absolute difference means
sum of even numbers-sum of odd numbers
in a given list'''
