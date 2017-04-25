#mapping the words to a real number space to encode it and form a feature vector for the neural network.

import numpy
import random
import math
import re

#cLang = "spanish"
cLang = "english"
langFile =  cLang+"_toEncoderavgLen.txt"

writer = open(cLang+"_toEncoderNums.txt", "w")

dictio = dict()

with open(cLang+"_EwordNumberMap.txt", "r") as file:
	for line in file:
		line = line.split(',')
		dictio[line[0]] = line[1].strip()
		print dictio[line[0]]



with open(langFile, "r") as file:
	for line in file:
		numSent=""
		line = line.split()

		for i in range(0,len(line)):
			x = dictio[line[i]]
			numSent = numSent+str(x)+" "

		writer.write(numSent+"\n")

writer.close()
#writer = open('eng.txt', 'w')
