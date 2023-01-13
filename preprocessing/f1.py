import re

def getDate(string):
	return re.sub(r"Date: ","",string)
def getFrom(string):
	return re.sub(r"From: ","",string)
def getTo(string):
	return re.sub(r"To: ","",string)
def getSubject(string):
	return re.sub(r"Subject: ","",string)
def getMessage(l):
	j = None
	for i in range(len(l)):
		#get index of subject
		if re.search("Subject: ", l[i]) != None:
				j = i
				break
	#if subject exists
	if j != None:
		temp = ""
		for i in range(j+1,len(l)):
			temp += l[i]
		return temp
	else:
		return False

def conf(arrText):
	obj = {"date":0,"from":"","to":"","subject":"","message":""}
	for i in arrText:
		if re.search("Date: ", i) != None:
			obj["date"] = getDate(i)
		elif re.search("From: ", i) != None:
			obj["from"] = getFrom(i)
		elif re.search("To: ", i) != None:
			obj["to"] = getTo(i)
		elif re.search("Subject: ", i) != None:
			obj["subject"] = getSubject(i)
		aux = getMessage(arrText)
		if aux != False:
			obj["message"] = aux 
	return obj


def func(filename):
	l = []
	with open(filename,"r") as f:
		l = f.read()
		l = re.sub(r"\t","",l)
		l = re.sub(r"  ","",l)
		#remove X-FileName
		l = re.sub(r"X-FileName: .*\n","",l)
		l = re.sub(r"X-Folder: .*\n","",l)
		l = re.sub(r"X-Origin: .*\n","",l)
		l = re.sub(r"X-From: .*\n","",l)
		l = re.sub(r"X-To: .*\n","",l)
		l = re.sub(r"X-cc: .*\n","",l)
		l = re.sub(r"X-bcc: .*\n","",l)
		l = re.sub(r"Content-Type: .*\n","",l)
		l = re.sub(r"Mime-Version: .*\n","",l)
		l = re.sub(r"Content-Transfer-Encoding: .*\n","",l)
		l = re.sub(r" \n","",l)
		l = re.sub(r"'","",l)
		l = re.sub(r'"',"",l)
		#l = re.sub(r"\n\n","",l)

		l = l.split("\n")

	return conf(l)

