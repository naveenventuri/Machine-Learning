import numpy as np
import matplotlib.pyplot as plt
import operator
points=np.array([[1,2],[5,4],[4,5],[6,3],[7,3],[8,2],[9,4],[10,1]])
points=np.array(sorted(points,key=operator.itemgetter(0)))
print(points)
x=points[:,[0]]
print(x)
y=points[:,[1]]
print(y)
one=np.ones((len(x),1),dtype=int)
print(one)
a=np.append(x**2,x,axis=1)
a=np.append(a,one,axis=1)
b=a.transpose()
c=b.dot(a)
print(c)
d=np.linalg.inv(c)
e=b.dot(y)
f=d.dot(e)
curve=f[0]*x**2+f[1]*x+f[2]
plt.scatter(x,y)
plt.plot(x,curve,'r')
plt.show()
