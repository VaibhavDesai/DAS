import datetime
import os
from pymongo import *
import random


def handle_uploaded_file(f,username):
	file_name = f.name
	file_path = '/Users/vaibhavdesai/Documents/college/research/DAS/audit/media/'+username+"/"+datetime.date.__str__(datetime.datetime.now())
	os.makedirs(file_path)
	with open(file_path+"/"+file_name, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
	split_file(file_path,file_name)

	db = Connection()["Research"]["files"]
	file_details = {"Owner":username,"file_name":file_name,"size":f.size,"datetime":datetime.date.__str__(datetime.datetime.now()),"verify":False,"FileId":random.randint(0,100000)}
	db.insert(file_details)

def split_file(file_path,file_name):
	contents = open(file_path+"/"+file_name,"r")
	total_size = len(contents.read())
	contents.seek(0,0)
	block_size = 500
		
	total_iterations = total_size/block_size
	remaining_size = total_size%block_size

	i = 0
	while i != total_iterations:	
		newFileText = open(file_path+"/"+"file"+str(i),"wb")
		text = contents.read(block_size)
		newFileText.write(text)
		newFileText.close()
		i = i+1

	if remaining_size != 0:
		newFileText = open(file_path+"/"+"file"+str(i),"wb")
		text = contents.read()
		newFileText.write(text)
		newFileText.close()
	print "the file are divied into" + str(total_iterations) + "files"