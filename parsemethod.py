import os
import sys
import re

def putoradd(key, val, res):
	if key != '' and val != '':
		if res.has_key(key):
			lis = res[key]
			lis.append(val)
		else:
			res[key] = [val]

def parsemethod(target):
	sp = target.split()
	p = re.compile(r'.+\(\)')
	for s in sp:
		m = p.match(s)
		if m != None:
			return m.group().replace('()', '')

def matchname(s):
	p = re.compile(r'.+Test\.java')
	m = p.match(s)
	if m != None:
		return True
	else:
		return False

def readfile(filename):
	f = open(filename)
	lines = f.readlines()
	f.close()
	return lines

def writefile(filename, data):
	f = open(filename, 'w')
	for d in data:
		f.write(d)
		f.write('\r\n')
	f.close()

def parsefile(filepath, filename):
	lines = readfile(filepath)
	r = {}
	for i in range(0, len(lines)):
		line = lines[i]
		trimmed = line.strip()
		if trimmed == "@Test":
			putoradd(filename, parsemethod(lines[i + 1].strip()), r)
	return r

def main(rootdir):
	R = {}
	for folder, subs, files in os.walk(rootdir):
		for filename in files:
			if matchname(filename):
				filepath = os.path.join(folder, filename)
				res = parsefile(filepath, filename)
				R = dict(R.items() + res.items())
	return R

def tocsv(data):
	L = []
	for key in data.keys():
		for v in data[key]:
			L.append(key + "," + v)
	return L

rootdir = sys.argv[1]
resultfile = 'result.txt'
mapres = main(rootdir)
writefile(resultfile, tocsv(mapres))
