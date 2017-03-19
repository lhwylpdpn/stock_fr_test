#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import os
import random
import time
import numpy as np
import sys
def load_data(name):
	data=[]
	f=open(name)
	#print(len(f.readlines()[1:-1]))
	file=f.readlines()[1:-1]
	for line in file:
		data.append(float(line.split(",")[-2]))
	f.close()

	print(name,np.std(data),sum(data)/len(data),np.std(data)/(sum(data)/len(data)))

if __name__ == '__main__':
	# files =  os.listdir("C:\Users\liuhao\Documents\minutes")
	# for x in files:
	# 	load_data("C:\Users\liuhao\Documents\minutes\\"+x)
	v1=[1,2,3,4,5]
	v2=[2,3,4,5,6]
	v=list(map(lambda x: x[0]-x[1], zip(v1, v2)))
	print(zip)