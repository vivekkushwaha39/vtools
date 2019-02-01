import re

file1 = "vpay-ihextags.txt"
file2 = "gvpay-ihextags.txt"

file1Tags = []
file2Tags = []

reg = re.compile('TAG_[A-Z|0-9]*')

file1Handle = open(file1,'r')
file2Handle = open(file2,'r')

while True :
	text = file1Handle.readline();
	if text == '':
		break;
	
	s1 = reg.search(text)
	if s1 is not None :
		file1Tags.append( s1.group() )
	

while True :
	text = file2Handle.readline();
	if text == '':
		break;
	s1 = reg.search(text)
	if s1 is not None :
		file2Tags.append(s1.group())

		
for i in file1Tags:
	if i not in file2Tags:
		print  ( i ,' Tag is not available in GVPAY')