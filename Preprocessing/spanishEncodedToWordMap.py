import numpy
import random
import math
import re
import sys
import mpmath
import pandas as pd
from mpmath import mp
from mpmath import mpf

dictio = dict()

cLang = "spanish"

avgLenSentences = cLang+"_toEncoderavgLen.txt"

#nums = "spanish_Encoder_matrix.txt"

spanishToWordMap = open("spanishToWordMap.txt",'w')

df1=pd.read_csv("SpanishMapKeys.csv",header=None,sep=',')
lNum=0
with open(avgLenSentences, "r") as file:
	for line in file:
		line = line.strip().split()
		#encode=avgLenSentences.readline().strip().split()
		for z in range(0,df1.shape[1]):
			n=str(df1.iloc[lNum:lNum+1,z:z+1])
			print n
			if(not(n in dictio)):
				dictio[n] = line[z]
#				print str(line[z])+"    :    "+str(n)
				spanishToWordMap.write(str(line[z])+","+str(n)+ "\n")
				#print line[z]
		lNum=lNum+1

for key in dictio:
	spanishToWordMap.write(str(key) + "," + str(dictio[key]) + "\n")

spanishToWordMap.close()