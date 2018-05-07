import matplotlib.pyplot as plt
import math as m
import numpy as np
data=[[10,1],[20,1],[32,0],[29,1],[30,0]]
w0=0.01
w1=0.01
for row in data:
	yhat=1/(1+m.exp(-w0-w1*row[0]))
	print("Expected=%.3f Predicted=%.3f[%d]"%(row[-1],yhat,round(yhat)))
plt.show()