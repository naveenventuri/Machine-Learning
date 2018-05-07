import numpy as np
import matplotlib.pyplot as plt
dataset=np.array([[0,0,0],[0,1,0],[1,0,0],[1,1,1]])
x1=dataset[:,[0]]
x2=dataset[:,[1]]
weights=[0.0 for i in range(len(dataset[0]))]
weights[0]=-0.6
weights[1]=0.3
weights[2]=0.2
print(len(dataset))
learning=0.1
for row in dataset:
	print("naveen")
	expected=row[-1]
	activation=weights[0]
	for i in range(len(row)-1):
		activation+= weights[i+1]*row[i]
	if(activation>0):
		prediction=1
	else:
		prediction=0;
	print("prediction=%d,Expected=%d,error=%d"%(prediction,expected,expected-prediction))
	weights[0]+=learning*(expected-prediction)
	for i in range(len(row)-1):
		print("%d"%(i+1))
		weights[i+1]+=learning*(expected-prediction)*row[i]
print(weights)
line=-(weights[0]/weights[2])-(weights[1]/weights[2])*x1
plt.scatter(x1,x2)
plt.plot(x1,line,'r')
plt.show()
