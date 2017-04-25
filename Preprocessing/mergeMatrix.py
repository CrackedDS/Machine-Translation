#merge the datasets for the input to the neural network

import pandas as pd

english="en_inputMatrix.csv"
spanish="sp_inputMatrix.csv"

sp=open(spanish,'r')

out = open("inputMatrix.csv",'w')
i=0

with open(english,'r') as en:
	for enline in en:
		enline=enline.strip()

		spline=sp.readline().strip()

		enline=enline+","+spline
		out.write(enline+"\n")
		i+=1
		print i
out.close()
