#Forming a dictionary between the Numbers and the Words for decoding the Spanish sentences after neural net process.

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
#cLang = "english"

avgLenSentences = cLang+"_toEncoderavgLen.txt"

#writer = open(cLang+"_num_matrix.txt", "w")

#wordsNumMap = open(cLang+"_EwordNumberMap.txt", "w")
writer = open("spanishToWordMap.txt",'w')
wordsNumMap = open("SpanishMapKeys.csv", "r")
#numbersAvgLen = cLang+"_nums_avgLen.txt"

with open(avgLenSentences, "r") as file:
	for line in file:
		line = line.split()
		en=wordsNumMap.readline().split(',')

		for z in range(0,len(en)):
			encode="0."+en[z].split('.')[1].split('e')[0]
			if(not(line[z] in dictio)):
				dictio[line[z]] = encode
				print line[z]

for key in dictio:
	writer.write(str(key) + "," + str(dictio[key]) + "\n")

writer.close()
