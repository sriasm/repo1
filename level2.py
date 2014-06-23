#!/usr/local/bin/python

'''
Program Name : Python Challange level 2
Written By   : Srini
Purpose      : For learning the program

'''

str1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

for x in str1:
	if ord(x)>=ord('a') and ord(x)<=ord('z'):
		list+=chr((ord(x)+2-ord('a'))+ord('a'))
	else:
		list+=x
print (list)