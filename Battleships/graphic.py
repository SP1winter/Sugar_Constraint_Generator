import numpy as np

#input hints
m = 0
n = 0
bs = 0
ha = np.array([])
rh = np.array([])
ch = np.array([])
#filename here!
with open("battleships_sample1p.txt", "r") as p:
	#size
	header = p.readline()
	size = header.split()
	m = int(size[0])
	n = int(size[1])
	bs = int(size[2])

	#column hints
	hint = p.readline()
	chstr = hint.split()
	tch = np.zeros((n+1, ), dtype=np.int)
	for j in range(0, n+1):
		if(chstr[j] == "-"):
			tch[j] = -1
		else:
			tch[j] = int(chstr[j])
	ch = tch

	#row hints & board
	ta = np.zeros((m+1, n+1), dtype=np.int)
	trh = np.zeros((m+1, ), dtype=np.int)
	for i in range(1, m+1):
		line = p.readline()
		row = line.split()
		if(row[0] == "-"):
			trh[i] = -1
		else:
			trh[i] = int(row[0])
		for j in range(1, m+1):
			# 7 wave
			# 1 up
			# 2 down
			# 3 left
			# 4 right
			# 5 center
			# 6 single
			if(row[j] == "w"):
				ta[i][j] = 7
			if(row[j] == "u"):
				ta[i][j] = 1
			if(row[j] == "d"):
				ta[i][j] = 2
			if(row[j] == "l"):
				ta[i][j] = 3
			if(row[j] == "r"):
				ta[i][j] = 4
			if(row[j] == "c"):
				ta[i][j] = 5
			if(row[j] == "s"):
				ta[i][j] = 6
	ah = ta
	rh = trh 

a = np.zeros((m+1, n+1), dtype=np.int)

p = open("result.txt", "r")
q = open("graphic.txt", "a")
chrlist = [".", "u", "d", "l", "r", "c", "s", "w"]

# input result
for i in range(1, m+1):
	for j in range(1, n+1):
		line = p.readline()
		wo = line.split()
		a[i][j] = int(wo[2])

# outout result
print("{0} {1} {2}".format(m,n,bs), file=q)
# column hints
for j in range(0, n+1):
	if(ch[j] == -1):
		print("- ", end="", file=q)
	else:
		print("{} ".format(ch[j]), end="", file=q)
print(file=q)
# row hints and board
for i in range(1, m+1):
	if(rh[i] == -1):
		print("- ", end="", file=q)
	else:
		print("{} ".format(rh[i]), end="", file=q)
	for j in range(1, n+1):
		if(ah[i][j] > 0):
			print(chrlist[ah[i][j]]+" ", end="", file=q)
		elif(a[i][j] == 1):
			print("o ", end="", file=q)
		else:
			print(". ", end="", file=q)
	print(file=q)

p.close()
q.close()