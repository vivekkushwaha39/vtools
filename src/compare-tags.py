import os
import re 


map1={}
map2={}

reg = re.compile('>[A-Z|0-9]*</')

file1Name='P400.log'
file2Name='MX9.log'

f1=open(file1Name, 'r')
f2=open(file2Name, 'r')



while( True ):
	key = f1.readline()

	if key=='':
		print 'err'
		break;
	
	val = f1.readline()
	
	if val == '':
		print 'err'
		break;

	search1 = reg.search(key)
	key = search1.group()
	
	
	
	search1 = reg.search(val)
	val = search1.group()
	
	
	# print key[1 : len(key)-2] + '=>' + val[1 : len(val)-2]
	map1[ key[1 : len(key)-2] ] = val[1 : len(val)-2]
	
# print map1

while( True ):
	key = f2.readline()

	if key=='':
		print 'err'
		break;
	
	val = f2.readline()
	
	if val == '':
		print 'err'
		break;

	search1 = reg.search(key)
	key = search1.group()
	
	
	
	search1 = reg.search(val)
	val = search1.group()
	
	
	# print key[1 : len(key)-2] + '=>' + val[1 : len(val)-2]
	map2[ key[1 : len(key)-2] ] = val[1 : len(val)-2]
	
# print map2

for k in map1:
	if k not in map2.keys()  :
		print repr(k).rjust(6), repr(map1[k]).rjust(80) ,'NA', repr('NOT AVAILABLE').rjust(80)
	elif map2[k] == map1[k] :
		print repr(k).rjust(6), repr(map1[k]).rjust(80) ,'==', repr(map2[k]).rjust(80)
	else :
		print repr(k).rjust(6), repr(map1[k]).rjust(80) ,'!=',repr(map2[k]).rjust(80)
		
for k in map2:
	if k not in map1.keys() :
		print 'NA in GVPAY:', k, ':', map2[k]
