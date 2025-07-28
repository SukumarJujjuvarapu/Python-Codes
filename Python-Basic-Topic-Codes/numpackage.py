import numpy as np
# a=np.array([0,1,0,4,1,7])
# b=np.array([[1,2],[3,4]])
# c=np.array([[[[1,2,3],[4,5,6],[7,8,9]]]]  )

# print(len(c))
# print(c.ndim)


# a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
# print(a.ndim)
# print(a.shape)
# print(a[:,2])
# a[1,2]=407
# print(a)

##zeros and ones

# a=np.zeros((4,4),dtype=int)
# b=np.ones((4,4),dtype=int)
# c=a+b
# print(a)
# print(b)


a=np.full((5,3),40)
b=np.random.rand(5,5)
c=np.random.randint(1,50,size=(5,5))
d=np.identity(5)
print(a)
print(b)
print(c)
print(d)