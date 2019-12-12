import numpy as np

#meta info
m = 0
n = 0
exhi = np.array([])
hint = np.array([])
dire = np.array([])

direction = {
	"U": 1,
	"L": 2,
	"D": 3,
	"R": 4,
	"?": -1,
}
test = 0

#filename here!
with open("yajilin_sample1p.txt", "r") as inp:
	#size
	header = inp.readline()
	size = header.split()
	m = int(size[0])
	n = int(size[1])


	#hints
	exhi_t = np.zeros((m+2, n+2), dtype=np.int)
	hint_t = np.zeros((m+2, n+2), dtype=np.int)
	dire_t = np.zeros((m+2, n+2), dtype=np.int)
	for i in range(0, m+2):
		for j in range(0, n+2):
			hint_t[i][j] = -2
			dire_t[i][j] = -2
	for i in range(1, m+1):
		getrow = inp.readline()
		row = getrow.split()
		for j in range(1, n+1):
			arrow = row[j-1]
			if(arrow == "??"):
				exhi_t[i][j] = 1
				hint_t[i][j] = -1
				dire_t[i][j] = -1
			elif(arrow != "--"):
				exhi_t[i][j] = 1
				hint_t[i][j] = int(arrow[0])
				dire_t[i][j] = direction[arrow[1:2]]
	exhi = exhi_t
	hint = hint_t
	dire = dire_t

#output
out = open("yajilin.csp", "w")
#definitions
#line
print(";definitions", file=out)
for i in range(1, m):
	for j in range(1, n+1):
		print("(int v_{0}_{1} -1 1)".format(i, j), file=out)
for i in range(1, m+1):
	for j in range(1, n):
		print("(int h_{0}_{1} -1 1)".format(i, j), file=out)
#degree
print("(domain d (0 2))", file=out)
for i in range(1, m+1):
	for j in range(1, n+1):
		if(exhi[i][j] == 0):
			print("(int x_{0}_{1} d)".format(i, j), file=out)
		else:
			print("(int x_{0}_{1} -1)".format(i, j), file=out)
#counting
for i in range(1, m+1):
	for j in range(1, n+1):
		print("(int z_{}_{} 0 {})".format(i, j, m*n), file=out)
		print("(int r_{}_{} 0 1)".format(i, j), file=out)

#lines out of bounds
print(";line out of bounds", file=out)
for i in range(1, m+1):
#	print("(int x_{0}_{1} -1)".format(i, 0), file=out)
	print("(int h_{0}_{1} 0)".format(i, 0), file=out)
#	print("(int x_{0}_{1} -1)".format(i, n+1), file=out)
	print("(int h_{0}_{1} 0)".format(i, n), file=out)

for j in range(1, n+1):
#	print("(int x_{0}_{1} -1)".format(0, j), file=out)
	print("(int v_{0}_{1} 0)".format(0, j), file=out)	
#	print("(int x_{0}_{1} -1)".format(m+1, j), file=out)
	print("(int v_{0}_{1} 0)".format(m, j), file=out)


#hints
print(";hints", file=out)
for i in range(1, m+1):
	for j in range(1, n+1):
		#upper
		if(dire[i][j] == 1):
			print("(count 0 (", end="", file=out)
			for k in range(1, i):
				print("x_{0}_{1} ".format(k, j), end="", file=out)
			print(") eq {})".format(hint[i][j]), file=out)
		#left
		if(dire[i][j] == 2):
			print("(count 0 (", end="", file=out)
			for l in range(1, j):
				print("x_{0}_{1} ".format(i, l), end="", file=out)
			print(") eq {})".format(hint[i][j]), file=out)
		#down
		if(dire[i][j] == 3):
			print("(count 0 (", end="", file=out)
			for k in range(i+1, m+1):
				print("x_{0}_{1} ".format(k, j), end="", file=out)
			print(") eq {})".format(hint[i][j]), file=out)
		#right
		if(dire[i][j] == 4):
			print("(count 0 (", end="", file=out)
			for l in range(j+1, n+1):
				print("x_{0}_{1} ".format(i, l), end="", file=out)
			print(") eq {})".format(hint[i][j]), file=out)

#loop 
# if x_i_j 0 then 
#(=> (or (= x_i_j) () () () ))
print(";rule of loops", file=out)
for i in range(1, m):
	for j in range(1, n+1):
		print("(=> (= x_{0}_{1} 0) (= v_{2}_{3} 0))".format(i, j, i, j), file=out)
		print("(=> (= x_{0}_{1} 0) (= v_{2}_{3} 0))".format(i+1, j, i, j), file=out)
		print("(=> (= x_{0}_{1} -1) (= v_{2}_{3} 0))".format(i, j, i, j), file=out)
		print("(=> (= x_{0}_{1} -1) (= v_{2}_{3} 0))".format(i+1, j, i, j), file=out)
for i in range(1, m+1):
	for j in range(1, n):
		print("(=> (= x_{0}_{1} 0) (= h_{2}_{3} 0))".format(i, j, i, j), file=out)
		print("(=> (= x_{0}_{1} 0) (= h_{2}_{3} 0))".format(i, j+1, i, j), file=out)
		print("(=> (= x_{0}_{1} -1) (= h_{2}_{3} 0))".format(i, j, i, j), file=out)
		print("(=> (= x_{0}_{1} -1) (= h_{2}_{3} 0))".format(i, j+1, i, j), file=out)

for i in range(1, m+1):
	for j in range(1, n+1):
		if(exhi[i][j] == 0):
			print("(= (+ (abs v_{0}_{1}) (abs v_{2}_{3}) (abs h_{4}_{5}) (abs h_{6}_{7}) ) x_{8}_{9} )"\
				.format(i-1, j, i, j, i, j-1, i, j, i, j), file=out)
			print("(= (+ v_{0}_{1} (neg v_{2}_{3}) h_{4}_{5} (neg h_{6}_{7}) ) 0)"\
				.format(i-1, j, i, j, i, j-1, i, j), file=out)
#not adjacent
print(";not adjacent", file=out)
for i in range(1, m):
	for j in range(1, n+1):
		print("(or (not(= x_{0}_{1} 0)) (not(= x_{2}_{3} 0)))".format(i, j, i+1, j), file=out)
for i in range(1, m+1):
	for j in range(1, n):
		print("(or (not(= x_{0}_{1} 0)) (not(= x_{2}_{3} 0)))".format(i, j, i, j+1), file=out)

#loop uniqueness
print(";loop uniqueness", file=out)
for i in range(1, m+1):
	for j in range(1, n+1):
		print("(iff (> z_{0}_{1} 0) (> x_{2}_{3} 0))". format(i, j, i, j) ,file=out)
		print("(iff (= r_{0}_{1} 1) (= z_{2}_{3} 1) )". format(i, j, i, j) ,file=out)

print("(= (+ ", end="", file=out)
for i in range(1, m+1):
	for j in range(1, n+1):
		print("r_{0}_{1} ".format(i, j), end="", file=out)
print(") 1)", file=out)

for i in range(1, m):
	for j in range(1, n+1):
		print("(=> (> v_{0}_{1} 0) (or (< z_{2}_{3} z_{4}_{5}) (= z_{6}_{7} 1)))"\
			.format(i, j, i, j, i+1, j, i+1, j), file=out)
		print("(=> (< v_{0}_{1} 0) (or (> z_{2}_{3} z_{4}_{5}) (= z_{6}_{7} 1)))"\
			.format(i, j, i, j, i+1, j, i, j), file=out)
for i in range(1, m+1):
	for j in range(1, n):
		print("(=> (> h_{0}_{1} 0) (or (< z_{2}_{3} z_{4}_{5}) (= z_{6}_{7} 1)))"\
			.format(i, j, i, j, i, j+1, i, j+1), file=out)
		print("(=> (< h_{0}_{1} 0) (or (> z_{2}_{3} z_{4}_{5}) (= z_{6}_{7} 1)))"\
			.format(i, j, i, j, i, j+1, i, j), file=out)
out.close()