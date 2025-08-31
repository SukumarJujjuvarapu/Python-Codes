#WAPTP HOW MANY CONSONANTS PRESENT IN A GIVEN STRING


s=input()
v="AEIOUaeiou"
c=0         
for ele in s:
    if ele not in v:
        c+=1
print(c)



'''taking string input from user'''
'''assuming tha there are no vowels initially and taking count c as variable'''
'''for loop starts
s=sukumar
iteration 1
ele=s
s not in v
c=1

 iteration 2
 ele=u
 u is in v
 c=1
 
 iteretaion 3
  ele=k
 k is not in v
 c=2
 
  iteration 4
 ele=u
 u is in v
 c=2
 
  iteration 5
 ele=m
 m is not in v
 c=3

  iteration 6
 ele=a
 a is in v
 c=4

   iteration 7
 ele=r
 m is not in v
 c=4
 '''
