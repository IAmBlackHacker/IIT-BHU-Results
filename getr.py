import sys
try:
	import hashlib
	import webbrowser
	import pickle
except:
	print('install first hashlib,webbrowser\n   python -m pip install pickle\n   python -m pip install hashlib\n   python -m pip install webbrowser\nThis code will run on python 3.x')
	sys.exit(0)
import os
N=str(input('Enter Roll : '))
maps=pickle.load(open('Finals','rb'))
# for i in open('final.txt').readlines():
# 	i=i.strip().split()
# 	maps[i[0]]=i[1]
if N in maps.keys():
	has=hashlib.md5(N.encode('utf-8')).hexdigest()
	cmd='http://10.1.131.10/grade_sheet/index.php?sname='+N+'&sid='+maps[N]+'&msname='+has+'&ms1=95aea4c3483c560373356d1ba3fd73cc'
	webbrowser.open(cmd)
else:
	print('Enter Valid Roll')
	os.system('pause')	