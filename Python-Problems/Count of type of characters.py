#WAPTP HOW MANY SPECIAL CHRACATERS,ALPHABETS,DIGITS PRESENT IN A GIVEN STRING

s=input() 
SC=0       
DG=0
AL=0

for ele in s:       
    if ele.isalnum()==False:
        SC+=1
    elif ele.isalpha()==True:
        AL+=1
    else:
        DG+=1
print("Special characters are",SC)
print("Aplhabets are",AL)
print("Digits are",DG)



'''taking string input from user'''

'''assuming tha there are no special characters initially
                and taking SC as variable'''

'''assuming tha there are no alphabets initially
                and taking AL as variable'''

'''assuming tha there are no digits initially
                and taking DG as variable'''


'''iteration-1
 taking input as #H2@b
 now
 ele=H
 H isalpha==true
 AL=1'''

'''iteration-2
ele=2
 2 isdigit== true
 DG=1'''
 
'''iteration-3
ele=@
 @ isalnum==false
 sc=1
 '''

'''iteration-4
ele=b
 b is alpha== true
 al=1
 '''
