import numpy as np

#input
m = 0
n = 0
a = 0
h = np.array([])
e = np.array([])
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

#output
out = open("compass.csp", "w")

#definitions
for i in range(0, m):
	for j in range(0, n):
		print("(int x_{0}_{1} 0 {2})".format(i, j, a-1), file=out)
for i in range(0, m):
	for j in range(0, n):
		print("(int z_{0}_{1} 0 {2})".format(i, j, m*n-1), file=out)

#hints
for k in range(0, a):
	print("(= x_{0}_{1} {2})".format(h[k][0], h[k][1], k), file=out)
	print("(= z_{0}_{1} 0)".format(h[k][0], h[k][1]), file=out)
	#upper
	if(h[k][2] != -1 and h[k][0] > 0):
		print("(count {0} (".format(k), end="", file=out)
		for i in range(0, h[k][0]):
			for j in range(0, n):
				print("x_{0}_{1} ".format(i, j), end="", file=out)
		print(") eq {0})".format(h[k][2]), file=out)
	#down
	if(h[k][3] != -1 and h[k][0] < m-1):
		print("(count {0} (".format(k), end="", file=out)
		for i in range(h[k][0]+1, m):
			for j in range(0, n):
				print("x_{0}_{1} ".format(i, j), end="", file=out)
		print(") eq {0})".format(h[k][3]), file=out)
	#left
	if(h[k][4] != -1 and h[k][1] > 0):
		print("(count {0} (".format(k), end="", file=out)
		for i in range(0, m):
			for j in range(0, h[k][1]):
				print("x_{0}_{1} ".format(i, j), end="", file=out)
		print(") eq {0})".format(h[k][4]), file=out)
	#right
	if(h[k][5] != -1 and h[k][1] < n-1):
		print("(count {0} (".format(k), end="", file=out)
		for i in range(0, m):
			for j in range(h[k][1]+1, n):
				print("x_{0}_{1} ".format(i, j), end="", file=out)
		print(") eq {0})".format(h[k][5]), file=out)
	

#connectivity
dm = [-1, 0, 0, 1]
dn = [0, -1, 1, 0]
for i in range(0, m):
	for j in range(0, n):
		if(e[i][j] == 0):
			print("(or ", end="", file=out)
			for p in range(0, 4):
				ni = i + dm[p]
				nj = j + dn[p]
				if(0 <= ni and ni < m and 0 <= nj and nj < n):
					print("(and (= x_{0}_{1} x_{2}_{3}) (> z_{4}_{5} z_{6}_{7}) ) ".\
						format(i, j, ni, nj, i, j, ni, nj), end="", file=out)
			print(")", file=out)

out.close()