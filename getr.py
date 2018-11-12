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

def open_roll(N):
	maps=pickle.load(open('Finals','rb'))
	has=hashlib.md5(N.encode('utf-8')).hexdigest()
	if has in maps.keys():
		cmd='http://10.1.131.11/grade_sheet/index.php?sname='+N+'&sid='+maps[has]+'&msname='+has+'&ms1=95aea4c3483c560373356d1ba3fd73cc'
		webbrowser.open(cmd)
	else:
		print('\n\tEnter Valid Roll\t')
try:
	N=str(input('Enter Roll : '))
	open_roll(N)
except pickle.UnpicklingError:
	content = open('Finals','rb').read()
	with open('Finals','wb') as output:
		for line in content.splitlines():
			output.write(line + str.encode('\n'))
	open_roll(N)
except Exception as ex:
	print(ex)
	print('Messege Code Admin ...!')
