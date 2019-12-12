import numpy as np

#input
m = 0
n = 0
bs = 0
a = np.array([])
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
	a = ta
	rh = trh 

#output
out = open("battleships.csp", "w")

#definitions
for i in range(1, m+1):
	for j in range(1, n+1):
		print("(int x_{0}_{1} 0 1)".format(i,j), file=out)
for i in range(0, m+1):
	for j in range(0, n+1):
		print("(int z_{0}_{1} 0 {2})".format(i,j,bs), file=out)

#rule by clues
#board hints
for i in range(1, m+1):
	for j in range(1, n+1):
		#wave
		if(a[i][j] == 7):
			print("(= x_{0}_{1} 0)".format(i,j), file=out)
		#up
		if(a[i][j] == 1):
			print("(= x_{0}_{1} 1)".format(i,j), file=out)
			print("(= x_{0}_{1} 1)".format(i+1,j), file=out)
			if(i-1>0):
				print("(= x_{0}_{1} 0)".format(i-1,j), file=out)
		#down
		if(a[i][j] == 2):
			print("(= x_{0}_{1} 1)".format(i,j), file=out)
			print("(= x_{0}_{1} 1)".format(i-1,j), file=out)
			if(i+1<=m):
				print("(= x_{0}_{1} 0)".format(i+1,j), file=out)
		#left
		if(a[i][j] == 3):
			print("(= x_{0}_{1} 1)".format(i,j), file=out)
			print("(= x_{0}_{1} 1)".format(i,j+1), file=out)
			if(j-1>0):
				print("(= x_{0}_{1} 0)".format(i,j-1), file=out)
		#right
		if(a[i][j] == 4):
			print("(= x_{0}_{1} 1)".format(i,j), file=out)
			print("(= x_{0}_{1} 1)".format(i,j-1), file=out)
			if(j+1<=n):
				print("(= x_{0}_{1} 0)".format(i,j+1), file=out)
		#center
		if(a[i][j] == 5):
			print("(= x_{0}_{1} 1)".format(i,j), file=out)
			if(i == 1 or i == m):
				print("(= x_{0}_{1} 1)".format(i,j-1), file=out)
				print("(= x_{0}_{1} 1)".format(i,j+1), file=out)
			elif(j == 1 or j == n):
				print("(= x_{0}_{1} 1)".format(i-1,j), file=out)
				print("(= x_{0}_{1} 1)".format(i+1,j), file=out)
			else:
				print("(or (and (= x_{0}_{1} 1) (= x_{2}_{3} 1) )(and (= x_{4}_{5} 1) (= x_{6}_{7} 1) ) )" \
					.format(i-1,j,i+1,j,i,j-1,i,j+1),file=out)
		#only one
		if(a[i][j] == 6):
			print("(= x_{0}_{1} 1)".format(i,j), file=out)
			if(i-1>0):
				print("(= x_{0}_{1} 0)".format(i-1,j), file=out)
			if(i+1<=m):
				print("(= x_{0}_{1} 0)".format(i+1,j), file=out)
			if(j-1>0):
				print("(= x_{0}_{1} 0)".format(i,j-1), file=out)
			if(j+1<=n):
				print("(= x_{0}_{1} 0)".format(i,j+1), file=out)




#row hints
for i in range(1, m+1):
	if(rh[i] != -1):
		print("(= (+ ", end="", file=out)
		for j in range(1, n+1):
			print("x_{0}_{1} ".format(i,j) ,end="", file=out)
		print(") {0})".format(rh[i]), file=out)
#column hints
for j in range(1, n+1):
	if(ch[j] != -1):
		print("(= (+ ", end="", file=out)
		for i in range(1, m+1):
			print("x_{0}_{1} ".format(i,j) ,end="", file=out)
		print(") {0})".format(ch[j]), file=out)

#no touch diagonaly
for i in range(1, m):
	for j in range(1, n):
		print("(or (= x_{0}_{1} 0) (= x_{2}_{3} 0))".format(i, j, i+1 ,j+1), \
			file=out)
		print("(or (= x_{0}_{1} 0) (= x_{2}_{3} 0))".format(i+1, j, i ,j+1), \
			file=out)

#exceptional case
#all vertices are occupied
# (or (= x_{i}_{j} 1) (= x_{i+1}_{j} 1) (= x_{i}_{j+1} 1) (= x_{i+1}_{j+1}) )
if(m == 9 and n == 9 and bs == 5):
	for i in range(0,10):
		for j in range(0,10):
			print("(or ",end="",file=out)
			if(i>0 and j>0):
				print("(= x_{0}_{1} 1)".format(i,j),end="",file=out)
			if(i<m and j>0):
				print("(= x_{0}_{1} 1)".format(i+1,j),end="",file=out)
			if(i>0 and j<n):
				print("(= x_{0}_{1} 1)".format(i,j+1),end="",file=out)
			if(i<m and j<n):
				print("(= x_{0}_{1} 1)".format(i+1,j+1),end="",file=out)
			print(")",file=out)

#count length
for j in range(0, n+1):
	print("(= z_0_{0} 0)".format(j), file=out)
for i in range(1, m+1):
	print("(= z_{0}_0 0)".format(i), file=out)

for i in range(1, m+1):
	for j in range(1, n+1):
		print("(=> (= x_{0}_{1} 0) (= z_{2}_{3} 0))".format(i,j,i,j), file=out)
		print("(=> (= x_{0}_{1} 1) (= z_{2}_{3} (+ z_{4}_{5} z_{6}_{7} 1)))"\
			.format(i,j,i,j,i-1,j,i,j-1), file=out)
for k in range(1, bs+1):
	print("(count {0} (".format(k), end="", file=out)
	for i in range(1, m+1):
		for j in range(1, n+1):
			print("z_{0}_{1} ".format(i,j), end="", file=out)
	print(") eq {})".format((bs-k+1)*(bs-k+2)//2) , file=out)

out.close()
