#INPUT : [1,2,3,4,5,6]
#OUTPUT: ['odd','even','odd','even','even']

L=eval(input())
NL=[]
for ele in L:
    if ele%2==0:
        NL.append('even')
    else:
        NL.append('odd')
print(NL)
