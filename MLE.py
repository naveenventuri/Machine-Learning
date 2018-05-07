import numpy as np
import matplotlib.pyplot as plt
f, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)
prior=np.array([[0.1,0.2],[0.25,0.2],[0.5,0.2],[0.75,0.2],[1.0,0.2]])
x=prior[:,[0]]
y=prior[:,[1]]
print(x)
print(y)
ax1.stem(x, y)
H=5
T=5

like=pow(x,H)*pow(1-x,T)

ax2.stem(x,like)

posterior=like*y

ax3.stem(x,posterior)

plt.show()
