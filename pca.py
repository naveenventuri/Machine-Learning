import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch
import sys
import operator

# input
print("Please input the data points: ( One line for each point. Features in a point are separated by space )")

npmat = []

while 1:
    try:
        line = sys.stdin.readline()
    
        if not line or line.strip() == "" or line.strip() == "\n":
            break
    
        templist = [float(elem) for elem in line.split()]
        npmat.append(templist)
        
    except KeyboardInterrupt:
        print("Key board interrupted !!")
        break

npmat = np.matrix(npmat)
print(npmat[0].size)
# class to plot eigen values 
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

if npmat.shape == (1,0): # generate data in the absence of input
    print("No input argument for matrix. Continuing with random matrix. Random data points:")

    np.random.seed(2342347)
    mu_vecl =  np.array([0,0,0])
    cov_matl = np.array([[1,0,0],[0,1,0],[0,0,1]])
    npmat = np.random.multivariate_normal(mu_vecl, cov_matl, 20).T
    print(npmat)
if(npmat[0].size==2):
	plt.scatter([npmat[:,0]],[npmat[:,1]],color='blue')
	plt.show()
	all_samples = npmat
	# data measures (mean , scatter, covariance)
	mean_x = np.mean(all_samples[:,0])
	mean_y = np.mean(all_samples[:,1])
	mean_vector = np.array([[mean_x],[mean_y]])
	scatter_matrix = np.zeros((2,2))
	for i in range(all_samples.shape[0]):
		scatter_matrix += (all_samples[i,:].reshape(2,1) - mean_vector).dot((all_samples[i,:].reshape(2,1) - mean_vector).T)
	eig_val_sc, eig_vec_sc = np.linalg.eig(scatter_matrix)
	print(eig_vec_sc)
	plt.scatter([all_samples[:,0]], [all_samples[:,1]],color='green')
	plt.scatter([mean_x], [mean_y],color='red')
	i=0
	for v in eig_vec_sc.T:
		ax	= plt.axes()
		ax.arrow(mean_x,mean_y, v[0], v[1], head_width=0.05, head_length=0.1, fc='k', ec='k')
		i+=1
	plt.show()
	# Make a list of (eigenvalue, eigenvector) tuples
	eig_pairs = [(np.abs(eig_val_sc[i]), eig_vec_sc[:,i]) for i in range(len(eig_val_sc))]
	eig_pairs.sort(key=lambda x: x[0], reverse=True)
	print(eig_pairs[0][1].reshape(2,1))
	# transform data
	matrix_w = eig_pairs[1][1].reshape(2,1)
	transformed = matrix_w.T.dot(all_samples.transpose())
	print("Transformed data points:")
	print(transformed)

	# idx = eig_val_sc.argsort()[::-1]   
	# eigenValues = eig_val_sc[idx]
	# eigenVectors = eig_vec_sc[idx,:]
	# i=0
	# for v in eigenVectors.T:
		# print(v)
		# print(eigenValues[i])
		# i+=1
	# # plot transformed data
	plt.plot(transformed[0,0:20],0, 'o', markersize=7, color='blue', alpha=0.5)
	plt.xlim([-4,4])
	plt.ylim([-4,4])
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.legend()
	plt.title('Transformed samples')
	plt.show()


else:
	# plot the sample space
	fig = plt.figure(figsize=(8,8))
	ax = fig.add_subplot(111, projection='3d')
	plt.rcParams['legend.fontsize'] = 10
	ax.scatter(xs=npmat[0,:],ys=npmat[1,:], zs=npmat[2,:],color='blue')
	plt.title('Sample data points')
	plt.show()
	all_samples = npmat
	print(all_samples[0,:])
	# data measures (mean , scatter, covariance)
	mean_x = np.mean(all_samples[0,:])
	mean_y = np.mean(all_samples[1,:])
	mean_z = np.mean(all_samples[2,:])
	mean_vector = np.array([[mean_x],[mean_y],[mean_z]])
	scatter_matrix = np.zeros((3,3))
	for i in range(all_samples.shape[1]):
		scatter_matrix += (all_samples[:,i].reshape(3,1) - mean_vector).dot((all_samples[:,i].reshape(3,1) - mean_vector).T)
	# eigenvectors and eigenvalues for the from the scatter matrix	
	eig_val_sc, eig_vec_sc = np.linalg.eig(scatter_matrix)
	# plot eigen values
	fig = plt.figure(figsize=(7,7))
	ax = fig.add_subplot(111, projection='3d')
	ax.plot(all_samples[0,:], all_samples[1,:], all_samples[2,:], 'o', markersize=8, color='green', alpha=0.2)
	ax.plot([mean_x], [mean_y], [mean_z], 'o', markersize=10, color='red', alpha=0.5)
	for v in eig_vec_sc.T:
		a = Arrow3D([mean_x, v[0]], [mean_y, v[1]], [mean_z, v[2]], mutation_scale=20, lw=3, arrowstyle="-|>", color="r")
		ax.add_artist(a)
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')
	plt.title('Eigen vectors')
	plt.show()	
	# Make a list of (eigenvalue, eigenvector) tuples
	eig_pairs = [(np.abs(eig_val_sc[i]), eig_vec_sc[:,i]) for i in range(len(eig_val_sc))]
	eig_pairs.sort(key=lambda x: x[0], reverse=True)
	# transform data
	matrix_w = np.hstack((eig_pairs[0][1].reshape(3,1), eig_pairs[1][1].reshape(3,1)))
	transformed = matrix_w.T.dot(all_samples)
	print("Transformed data points:")
	print(transformed)

	# plot transformed data
	plt.plot(transformed[0,0:20], transformed[1,0:20], 'o', markersize=7, color='blue', alpha=0.5)
	plt.xlim([-4,4])
	plt.ylim([-4,4])
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.legend()
	plt.title('Transformed samples')
	plt.show()



    


