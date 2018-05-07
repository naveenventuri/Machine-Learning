import numpy as np
import matplotlib.pyplot as plt
N=2;
#PRIOR 
res=5;
theta=np.linspace(0,1,res)

prior=np.ones(res,dtype=float)
prior=prior/np.sum(prior)

f, (ax1, ax2, ax3,ax4) = plt.subplots(4, 1, sharex=True)

ax1.stem(theta, prior)

like=pow(theta,H)*pow(1-theta,T)

ax2.stem(theta,like)

#POSTERIOR
posterior=like*prior

ax3.stem(theta,posterior)

#NORMALIZED LIKELIHOOD
likenor=like/np.sum(like)

ax4.stem(theta,likenor)
plt.figure(2)
plt.stem(theta,likenor)

#P(D)
	

plt.show()