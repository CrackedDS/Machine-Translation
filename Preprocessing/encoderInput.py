#parsing the inpu5 line to pass as input to the encoder.

import numpy
import random
import math
import re
import sys
import mpmath
import pandas as pd
from mpmath import mp
from mpmath import mpf

df = pd.DataFrame()
mp.dps = 100

dictio = dict()

#cLang = "spanish"
cLang = "english"

avgLenSentences = open(cLang+"_toEncoderavgLen.txt", "r")

writer = open(cLang+"_Encoder_matrix.txt", "w")

#newWordsNumMap = open(cLang+"_EncodedWordNumberMap.txt", "w")

numbersAvgLen = cLang+"_toEncoderNums.txt"

max=0.0
min = sys.maxint

with open(numbersAvgLen, "r") as file:
	for line in file:
		line = line.split()

		for z in range(0,len(line)):
			n = float(line[z])

			if(n>max):
				max=n

			if(n<min):
				min = n


denom = max-min
val = 0.0

print max
print min

if(cLang == "spanish"):
	with open(numbersAvgLen, "r") as file:

		lno=0

		for line in file:
			line = line.split()
			sentence = []

			wordLine = avgLenSentences.readline().split()

			for z in range(0,len(line)):
				n = float(line[z])
				val = (max-n)/denom
				sentence.append(val)
				dictio[val] = str(wordLine[z])

			print str(len(sentence))+"  :  "+str(lno)
			lno=lno+1

			stringBuild=""
			for x in range(0,len(sentence)):
				stringBuild=stringBuild+str(sentence[x])+","

			writer.write(stringBuild[0:len(stringBuild)-1]+"\n")

writer.close()
