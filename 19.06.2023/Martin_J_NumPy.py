import numpy as np

a=np.array([[1,1],[2,2]])

b=np.array([[1,3],[-2,]])
c=a.dot(b)
print(c)

d=np.array([[1,-1j],[2,2j]])
e=np.array([[-1j,3],[-2,-3j]])
f=d.dot(e)
print(f)