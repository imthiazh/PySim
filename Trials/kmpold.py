import itertools


def kmp_search(pat, txt):
	M = len(pat)
	N = len(txt)


	lps = [0]*M
	j = 0


	computeLPSArray(pat, M, lps)

	i = 0
	while i < N:
		if pat[j] == txt[i]:
			i += 1
			j += 1

		if j == M:
			print (pat)
			j = lps[j-1]


		elif i < N and pat[j] != txt[i]:

			if j != 0:
				j = lps[j-1]
			else:
				i += 1

def computeLPSArray(pat, M, lps):
	len = 0


	i = 1


	while i < M:
		if pat[i]== pat[len]:
			len += 1
			lps[i] = len
			i += 1
		else:

			if len != 0:
				len = lps[len-1]


			else:
				lps[i] = 0
				i += 1



linelist1=[line.rstrip('\n') for line in open('facedetect.py','r')]
linelist2=[line.rstrip('\n') for line in open('facedetect2.py','r')]


def listToString(s):
	str1 = ""
	for ele in s:
		str1 += ele
	return str1
i=0
j=0

for a in linelist1:
	if (a==''): linelist1.remove(a)
for a in linelist2:
	if (a==''): linelist2.remove(a)

for(a,b) in zip(linelist1,linelist2):
	if i<len(linelist1) and j<len(linelist2):
	   kmp_search(a, b)
	   i+=1
	   j+=1