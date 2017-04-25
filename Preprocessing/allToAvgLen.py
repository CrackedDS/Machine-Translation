#Filters the Input Dataset to extract sentences of length between 26 and 29.

import numpy
import random
import math
import re

setAvgLen = 29

def concatLongNum(line):
	grouping = len(line)/setAvgLen
	nl=[]
	z=0
	ind=0
	while((z<len(line)) and ind<setAvgLen):
		x = line[z:(z+grouping)]
		tsum=0
		for wn in x:
			tsum = tsum+int(wn)
		tsum=tsum/grouping
		nl=nl+[tsum]
		ind=ind+1
		z=z+grouping
	return nl


def concatLongSent(line):
	grouping = len(line)/setAvgLen
	nl=[]
	z=0
	ind=0
	while((z<len(line)) and ind<setAvgLen):
		x = line[z:(z+grouping)]
		tsum=""
		for wn in x:
			tsum = tsum+wn
		nl=nl+[tsum]
		ind=ind+1
		z=z+grouping
	return nl

#cLang = "spanish"
cLang = "english"

#oLang = "english"
oLang = "spanish"

#numberWriter = open(cLang+'_nums_avgLen.txt', 'w')
wordWriter = open(cLang+'_toEncoderavgLen.txt', 'w')

spRead = open(oLang+'.txt', 'r')

wordNumbers = cLang+"_nums.txt"

originalF = cLang+".txt"

#nonsenseNum = ["111111"]
nonsenseWord = ["oo"]


#words
with open(originalF, 'r') as file:
	i = 0
	for line in file:
		spLine = spRead.readline().split()
		line = line.split()
		modline = line
		print len(modline)
		i+=1

		if(len(line)>setAvgLen or len(spLine)>setAvgLen or len(line)<26 or len(spLine)<26):
			continue

		while(len(modline)<setAvgLen):
			modline = modline + nonsenseWord
		
		else:
			fin = modline

#		fin = concatLongSent(modline)
		toWrite = ""

		for z in range(0,len(fin)):
			toWrite = toWrite + str(fin[z]) + " "

		wordWriter.write(toWrite[0:len(toWrite)-1] + "\n")
		print str(i) + "  :  " + str(len(fin))
wordWriter.close()
