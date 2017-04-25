#not used yet. Will contain the integration of everything in one final file

import numpy as np
import pandas as pd
import random
pd.set_option('precision',20)
np.set_printoptions(precision=20)

def sigmoid(x):
	return 1/(1 + np.exp(-x))


def formMatrix(file):
	data = pd.read_csv(file, header = None, sep = ',')
	df = pd.DataFrame(data = data, dtype = float)
	return df

def main():
	df = formMatrix('English_Weight_lvl1_36.csv')
	xenc = formMatrix('xinput.csv')
	xenc = df.iloc[0:1,0:29]
	xenc = np.array(xenc.values)
	xenc = np.append(xenc, 1)
	omega = df.iloc[:,:]
	omega = np.array(omega.values)
	yenc = sigmoid(np.dot(xenc, omega))
	np.savetxt("yenc.csv", yenc, delimiter = ",")
	x = formMatrix('yenc.csv')
	weights = formMatrix('NeuralWeights.csv')
	weights = df.iloc[:,:]
	weights = np.array(omega.values)
	#	[omega1, omega2, omega3, delta, bias, alpha1, alpha2, alpha3, beta1, beta2, beta3, gamma1, gamma2, gamma3, bias1, bias2, bias3, omega1hat, omega2hat, omega3hat]
	j = 0
	for i in range (0, 26):
		x[((j*26)+i),0] = (float(x[((j*26)+i),0]))
		x[((j*26)+i),1] = (float(x[((j*26)+i),1]))
		x[((j*26)+i),2] = (float(x[((j*26)+i),2]))
		y[((j*26)+i),0] = (float(y[((j*26)+i),0]))
		s1 = sigmoid(x[((j*26)+i),0] * omega1hat + bias1)
		s2 = sigmoid(x[((j*26)+i),1] * omega2hat + bias2)
		s3 = sigmoid(x[((j*26)+i),2] * omega3hat + bias3)
		g1 = sigmoid(alpha1 * s1 + beta1 * s2 + gamma1 * s3 + bias1)
		g2 = sigmoid(alpha2 * s1 + beta2 * s2 + gamma2 * s3 + bias2)
		g3 = sigmoid(alpha3 * s1 + beta3 * s2 + gamma3 * s3 + bias3)
		h1 = sigmoid(alpha1 * g1 + beta1 * g2 + gamma1 * g3 + bias1)
		h2 = sigmoid(alpha2 * g1 + beta2 * g2 + gamma2 * g3 + bias2)
		h3 = sigmoid(alpha3 * g1 + beta3 * g2 + gamma3 * g3 + bias3)
		o1 = sigmoid(alpha1 * h1 + beta1 * h2 + gamma1 * h3 + bias1)
		o2 = sigmoid(alpha2 * h1 + beta2 * h2 + gamma2 * h3 + bias2)
		o3 = sigmoid(alpha3 * h1 + beta3 * h2 + gamma3 * h3 + bias3)
		ypred[((j*26)+i),0] = sigmoid(omega1 * o1 + omega2 * o2 + omega3 * o3 + delta * ypredprev + bias)
		ypredprev = ypred[((j*26)+i),0]
			
	df = formMatrix('Spanish_Weight_lvl2_36.csv')
	df1 = formMatrix('YPredictions.csv')
	#print df.head()
#	cols = df1.shape[1]
#	rows = df1.shape[0]
	ypred = df1.iloc[0:26, 0:1]
	ypred = (np.transpose(np.array(ypred.values)))
	ypred = np.c_[ypred, np.ones((1,1))]
	print(ypred)
	omega = df.iloc[:,:]
	omega = np.array(omega.values)
	print(omega.shape)
	yout = sigmoid(np.dot(ypred, omega))
	np.savetxt("YFinal.csv", yout, delimiter = ",")
	#print(ytrain)
	#print(xtrain)
#	[omega1, omega2, omega3, delta, bias, alpha1, alpha2, alpha3, beta1, beta2, beta3, gamma1, gamma2, gamma3, bias1, bias2, bias3, omega1hat, omega2hat, omega3hat]
#	weights = np.zeros(20)
	#print(df.iloc[0:rows/2, 1:cols-1])
#	weights = rnnTrain(ytrain, xtrain)
#	np.savetxt("NeuralWeights.csv", weights, delimiter = ",")
#	xtest = df.iloc[rows/2:rows, 0:cols-1]
#	ytest = df.iloc[rows/2:rows, cols-1:cols]
#	xtest = np.array(xtest.values)
#	ytest = np.array(ytest.values)
#	accuracy, ypred, yfinal = rnnTest(ytest, xtest, weights)
#	np.savetxt("YPredictions.csv", ypred, delimiter = ",")
	#print(accuracy)
	#complete this with post processing of the data.
	
if __name__ == "__main__": main()
