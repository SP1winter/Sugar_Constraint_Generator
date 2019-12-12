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

#graphic
with open("graphic.txt", "a") as gra:
	print(m, n, file=gra)
	print("+   "* n + "+", file=gra)
	for i in range(1, m+1):
		#horizontal
		print("  ", end="", file=gra)
		for j in range(1, n+1):
			if(ans_x[i][j] == 0):
				print("#   ", end="", file=gra)
			elif(ans_x[i][j] == -1):
				if(dire[i][j]== -1):
					print("??  ", end="", file=gra)
				else:
					print(str(hint[i][j]) + list_dir[dire[i][j]] + "  "\
						, end="", file=gra)
			else:
				if(ans_h[i][j] == 0):
					print("+   ", end="", file=gra)
				else:
					print("+---", end="", file=gra)
		print(file=gra)
		#vertical
		print("+ ", end="", file=gra)
		for j in range(1, n+1):
			if(ans_v[i][j] == 0):
				print("  + ", end="", file=gra)
			else:
				print("| + ", end="", file=gra)
		print(file=gra)
