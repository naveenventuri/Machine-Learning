import numpy as np
import matplotlib.pyplot as plt
import itertools

N=2;
lst = list(itertools.product([0, 1], repeat=N))
print(lst)
z=np.zeros(pow(2,N))

for i in range(0,pow(2,N)):
	z[i]=np.count_nonzero(lst[i])
	print(z[i])
   
	
#PRIOR 
res=5;
theta=np.linspace(0,1,res)

prior=np.ones(res,dtype=float)
prior=prior/np.sum(prior)

sum_pos=np.zeros(4)

#LIKELIHOOD
 
for i in range(0,pow(2,N)):
	H=len(lst[i])-z[i]
	T=z[i]
	like=pow(theta,H)*pow(1-theta,T)
	posterior=like*prior
	sum_pos[i]=np.sum(posterior)
	
print(np.sum(sum_pos))
	

