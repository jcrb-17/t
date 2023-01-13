import os
from timeit import default_timer as timer
import f1
import re

start = timer()

path = "./"

def writeLog(text):
	with open("log","a") as f:
		f.write(text)
  
for subdir, dirs, files in os.walk(path):
	for f in files:
		if f.endswith("."):
			fullPath = os.path.join(subdir, f)
			try:
				c = re.sub(r"'",'"',str(f1.func(fullPath)))
				with open("db.ndjson","a") as f:
					f.write('{"index" : { "_index" : "db" } }\n') 
					f.write(c+"\n")
			except:
				print(fullPath)
				writeLog(fullPath)
				continue

end = timer()

t = (end - start)/60
print(t , "min")

writeLog(str(t) + " min")
