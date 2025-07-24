set={1,3,4,5,6,7,8,9,0}
print(type(set))

set.add(5440)
print(set)
set.pop()
set.remove(9)
print(set)
s1={98,76,54,32,980}
s2={323,54534,1313,678,54}
for i in s1:
    for j in s2:
        print(j)
print(i)
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.issuperset(s2))














