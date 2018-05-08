import numpy as np
import math
from sklearn import datasets
k_all=[1,5,10,20,40,100]
for i in range(len(k_all)):
	k=k_all[i]	
	sum=0
	digits=datasets.load_digits()
	data_and_labels = list(zip(digits.data, digits.target))
	train_data=np.array(digits.data[0:1212])
	train_label=np.array([digits.target[0:1212]])
	train_label=train_label.transpose()
	#train_data=np.concatenate((train_data,train_label),axis=1)
	test_data=np.array(digits.data[1212:1798])
	test_label=np.array([digits.target[1212:1798]])
	test_label=test_label.transpose()
	#test_data=np.concatenate((test_data,test_label),axis=1)
	def euc_dist(test_img,train_img):
			distance=0
			for i in range(len(train_img)):
				distance=distance+math.pow(test_img[i]-train_img[i],2)
			distance=math.sqrt(distance)
			return distance
		
	for i in range(len(test_data)):
		test_img_1=test_data[i,:]
		test_img_1_label=test_label[i,:]
		euc=np.full((len(train_data),1),0,dtype=float)
		for i in range(len(train_data)):
			euc[i]=euc_dist(test_img_1,train_data[i])
		euc=np.concatenate((euc,train_label),axis=1)
		euc = euc[euc[:,0].argsort()]
		vote=np.full((10,1),0,dtype=int)
		label=np.array([[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]])
		vote=np.concatenate((vote,label),axis=1)
		k_votes=euc[0:k,1]
		for i in range(len(k_votes)):
			if(k_votes[i]==0):
				vote[0][0]+=1
			if(k_votes[i]==1):
				vote[1][0]+=1
			if(k_votes[i]==2):
				vote[2][0]+=1
			if(k_votes[i]==3):
				vote[3][0]+=1
			if(k_votes[i]==4):
				vote[4][0]+=1
			if(k_votes[i]==5):
				vote[5][0]+=1
			if(k_votes[i]==6):
				vote[6][0]+=1
			if(k_votes[i]==7):
				vote[7][0]+=1
			if(k_votes[i]==8):
				vote[8][0]+=1
			if(k_votes[i]==9):
				vote[9][0]+=1
		vote = vote[vote[:,0].argsort()]
		# print("The Number is ",vote[9][1])
		# print("With votes =",vote[9][0])
		if(test_img_1_label==vote[9][1]):
			sum+=1
	print("accuracy=",sum/len(test_data))	