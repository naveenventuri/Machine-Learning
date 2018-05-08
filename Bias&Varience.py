import numpy as np
import math
import matplotlib.pyplot as plt
x=np.linspace(-1,1,100)
y=np.sin(np.pi*x)
h0=np.zeros((100,100))
h1=np.zeros((100,100))
for i in range (0,100):
	rand_num=np.random.randint(100,size=2)
	x1=x[rand_num[0]]
	x2=x[rand_num[1]]
	y1=y[rand_num[0]]
	y2=y[rand_num[1]]
	h0[:,i]=np.array([(y1+y2)/2 for i in range(len(x))])
	diff=x1-x2
	if(diff==0):
		diff = 0.1**6
	a=(y1-y2)/diff
	b=y1-a*x1
	h1[:,i]=a*x+b
avg0=np.zeros((100,1))
bias0=np.zeros((100,1))
var0=np.zeros((100,1))
var_up0=np.zeros((100,1))
var_down0=np.zeros((100,1))
avg1=np.zeros((100,1))
bias1=np.zeros((100,1))
var1=np.zeros((100,1))
var_up1=np.zeros((100,1))
var_down1=np.zeros((100,1))
for i in range (0,100):
	avg0[i]=sum(h0[i,:])
avg0=avg0/100
for i in range(0,100):
	bias0[i]=(avg0[i]-y[i])**2
print("bias1 = ",sum(bias0)/100)
for i in range(0,100):
	for j in range(0,100):
		var0[i]=var0[i]+(h0[i,j]-avg0[i])**2
	var0[i]=var0[i]/100
print("varience1 =",sum(var0)/100)
for i in range (0,100):
	var_up0[i]=avg0[i]+math.sqrt(var0[i])
	var_down0[i]=avg0[i]-math.sqrt(var0[i])
plt.figure(1)
plt.plot(x,y)
plt.plot(x,avg0,'ro')
plt.scatter(x,var_up0,color='grey')
plt.scatter(x,var_down0,color='grey')

for i in range (0,100):
	avg1[i]=sum(h1[i,:])
avg1=avg1/100
for i in range(0,100):
	bias1[i]=(avg1[i]-y[i])**2
print("bias2 =",sum(bias1)/100)
for i in range(0,100):
	for j in range(0,100):
		var1[i]=var1[i]+(h1[i,j]-avg1[i])**2
	var1[i]=var1[i]/100
print("varience =",sum(var1)/100)
for i in range (0,100):
	var_up1[i]=avg1[i]+math.sqrt(var1[i])
	var_down1[i]=avg1[i]-math.sqrt(var1[i])
plt.figure(2)
plt.plot(x,y)
plt.plot(x,avg1,'ro')
plt.scatter(x,var_up1,color='grey')
plt.scatter(x,var_down1,color='grey')
plt.show()
