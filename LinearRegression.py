import numpy as np
import matplotlib.pyplot as plt
import sys
import ast
x = np.linspace(0, 10, 30)
f = np.poly1d([5, 1])
y = f(x) + 6*np.random.normal(size=len(x))

print(x.shape)

print(y.shape)

npmat = np.column_stack((x, y))

print(npmat)

data = []
if len(sys.argv) > 1:    
    data = ast.literal_eval(sys.argv[1])
        
if len(data) == 0:
    print("No commandline input argument for matrix. Continuing with random matrix")
else:
    npmat = np.array(data)
print(npmat)
a = np.vstack([npmat[:,0], np.ones(len(npmat[:,0]))]).T
b=a.transpose()
c=b.dot(a)
print(c)
d=np.linalg.inv(c)
e=b.dot(y)
f=d.dot(e)
line=f[0]*x+f[1]
plt.scatter(x,y)
plt.plot(x,line,'r')
plt.show()
