import re
import os

filelist = os.listdir("C://Users/Sarah/Desktop/new book images")

filelist.sort()
pk = 2320
seq = 1
lastbook = 27

for name in filelist:
	m = re.search("M([0-9]+)_.*", name)
	book = m.group(1)
	
	if book == lastbook:
		seq += 1
	else:
		seq = 1
	
	lastbook = book 
		
	pk +=1
	
	print "{"
	print "\"pk\": {0}, ".format(pk)
	print "\"model\": \"BookExhibit.Bookimage\","
	print "\"fields\": {"
	print "\t\"image\":\"{0}\", ".format(name)
	print "\t\"sequence\": {0},".format(seq)
	print "\t\"book\": {0}".format(book)
	print "\t}"
	print "},\n"
	
