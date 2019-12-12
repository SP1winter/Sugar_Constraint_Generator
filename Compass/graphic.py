import numpy as np

#input hints
m = 0
n = 0
a = 0
h = np.array([])
e = np.array([])
ans = np.array([])
#filename here!
with open("compass_sample1p.txt", "r") as p:
	#size
	header = p.readline()
	size = header.split()
	m = int(size[0])
	n = int(size[1])
	a = int(size[2])

	th = np.zeros((a, 6), dtype=np.int)
	#hints
	for k in range(0, a):
		hint = p.readline()
		hstr = hint.split()
		for l in range(0, 6):
			if(hstr[l] == "-"):
				th[k][l] = -1
			else:
				th[k][l] = int(hstr[l])
	h = th

te = np.zeros((m, n), dtype=np.int)
for k in range(0, a):
	te[h[k][0]][h[k][1]] = 1
e = te


# input result
ans = np.zeros((m+1, n+1), dtype=np.int)
q = open("result.txt", "r")
r = open("graphic.txt", "a")

for i in range(0, m):
	for j in range(0, n):
		line = q.readline()
		wo = line.split()
		ans[i][j] = int(wo[2])
for i in range(0, m+1):
	ans[i][n] = -1
for j in range(0, n):
	ans[m][j] = -1 

# outout result easy
print(m, n, a, file=r)
for i in range(0, m):
	for j in range(0, n):
		print("{} ".format(ans[i][j]), end="", file=r)
	print(file=r)
print(file=r)
#output result hard
print("+ - "* n + "+", file=r)
for i in range(0, m):
	print("|", end="", file=r)
	for j in range(0, n):
		if(e[i][j] == 1):
			if(ans[i][j]<10):
				print(" {0} ".format(ans[i][j]), end="", file=r)
			elif(ans[i][j]<100):
				print("{0} ".format(ans[i][j]), end="", file=r)
			else:
				print("{0}".format(ans[i][j]), end="", file=r)
		else:
			print("   ", end="", file=r)
		if(ans[i][j] != ans[i][j+1]):
			print("|", end="", file=r)
		else:
			print(" ", end="", file=r)
	print(file=r)
	print("+", end="", file=r)
	for j in range(0, n):
		if(ans[i][j] != ans[i+1][j]):
			print(" - ", end="", file=r)
		else:
			print("   ", end="", file=r)
		print("+", end="", file=r)
	print(file=r)


q.close()
r.close()