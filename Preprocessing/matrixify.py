#convert the existing file into the proper matrix form for the neural net.

import numpy
import random
import math
import re
import sys
import mpmath
import pandas as pd
from mpmath import mp
from mpmath import mpf

l="en"
l="sp"

f = "yenc.csv"
#f=l+"_EncodedWords.csv"
#writer = open(l+"_inputMatrix.csv",'w')
writer = open("yenc.csv",'w')
if(l=="en"):
	with open(f, "r") as file:
		for line in file:
			line = line.strip().split(',')
			line=line+line[0:2]

			for i in range(0,len(line)-2):
				row = str(line[i])+","+str(line[i+1])+","+str(line[i+2])
				writer.write(str(row)+"\n")
	writer.close()

if(l=="sp"):
	with open(f, "r") as file:
		for line in file:
			line = line.strip().split(',')

			for i in range(0,len(line)):
				row = str(line[i])
				writer.write(str(row)+"\n")
writer.close()

