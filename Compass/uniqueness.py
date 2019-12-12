import numpy as np

m = 0
n = 0
a = 0
with open("compass_sample1p.txt", "r") as p0:
	header = p0.readline()
	size = header.split()
	m = int(size[0])
	n = int(size[1])

p = open("result.txt", "r")
q = open("compass.csp", "a")

print("(not (&& ", end="",file=q)
for i in range(0, m*n):
	line = p.readline()
	wo = line.split()
	print("(= {0} {1}) ".format(wo[1],wo[2]),end="",file=q)

print(") )",file=q)

p.close()
q.close()
