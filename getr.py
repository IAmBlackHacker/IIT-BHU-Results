import sys
import os
try:
	import hashlib
	import webbrowser
	import pickle
except:
	print('  Install first hashlib,webbrowser\n-------------------------------------------\n   python3 -m pip install pickle\n   python3 -m pip install hashlib\n   python3 -m pip install webbrowser\nThis code will run on Python Version 3.x')
	sys.exit(0)

if sys.version_info[0] != 3:
	print('\n------------------------------\n     USE PYTHON 3.x \n------------------------------\n')
	sys.exit(0)

try:
	N=str(input('Enter Roll : '))
	maps=pickle.load(open('Finals','rb'))
	has=hashlib.md5(N.encode('utf-8')).hexdigest()
	if has in maps.keys():
		cmd='http://10.1.131.10/grade_sheet/index.php?sname='+N+'&sid='+maps[has]+'&msname='+has+'&ms1=95aea4c3483c560373356d1ba3fd73cc'
		webbrowser.open(cmd)
	else:
		print('Enter Valid Roll')
		os.system('pause')	
except Exception as ex:
	print(ex)
