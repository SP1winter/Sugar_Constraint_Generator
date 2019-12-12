import numpy as np

m = 0
n = 0
with open("yajilin_sample1p.txt", "r") as p0:
	header = p0.readline()
	size = header.split()
	m = int(size[0])
	n = int(size[1])

#info for answer
ans_v = np.zeros((m+1, n+1), dtype=np.int)
ans_h = np.zeros((m+1, n+1), dtype=np.int)
ans_x = np.zeros((m+1, n+1), dtype=np.int)
list_dir = ["?", "U", "L", "D", "R"]

#input result
with open("result.txt", "r") as res:
	for i in range(1, m):
		for j in range(1, n+1):
			getver = res.readline()
			ver = getver.split()
			ans_v[i][j] = int(ver[2])
	for i in range(1, m+1):
		for j in range(1, n):
			gethor = res.readline()
			hor = gethor.split()
			ans_h[i][j] = int(hor[2])
	for i in range(1, m+1):
		for j in range(1, n+1):
			getdeg = res.readline()
			deg = getdeg.split()
			ans_x[i][j] = int(deg[2])

#uniqueness
with open("yajilin.csp", "a") as csp:
	print(";constraint for uniqueness", file=csp)
	print("(not (and ", end="", file=csp)
	for i in range(1, m):
		for j in range(1, n+1):
			if(ans_v[i][j] != 0):
				print("(= (abs v_{0}_{1}) 1) ".format(i, j), end="", file=csp)
			else:
				print("(= v_{0}_{1} 0) ".format(i, j), end="", file=csp)					
	for i in range(1, m+1):
		for j in range(1, n):
			if(ans_h[i][j] != 0):
				print("(= (abs h_{0}_{1}) 1) ".format(i, j), end="", file=csp)
			else:
				print("(= h_{0}_{1} 0) ".format(i, j), end="", file=csp)
	print("))", file=csp)

