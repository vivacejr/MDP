def abso(a):
	if a < 0 :
		return -a
	return a

nm = raw_input().split()
n = int(nm[0])
m = int(nm[1])

ary = [[0.0 for x in range(m)] for y in range(n)]

for i in range(n):
	a = raw_input().split()
	for j in range(m):
		ary[i][j] = float(a[j])



ew = raw_input().split()
e = int(ew[0])
w = int(ew[1])

End = []
Wall = []

for i in range(e):
	tp = raw_input().split()
	a = int(tp[0]) 
	b = int(tp[1]) 
	End.append((a,b))

for i in range(w):
	tp = raw_input().split()
	a = int(tp[0]) 
	b = int(tp[1]) 
	Wall.append((a,b))

st = raw_input()

reward = float(input())

U = [[0.0 for x in range(m)] for y in range(n)] 
var = 1
inf = 100000000.0
dis = 0.99
for i in range(e):
	U[End[i][0]][End[i][1]]=ary[End[i][0]][End[i][1]]

setE = set(End)
setW = set(Wall)
reward = -2.7
error = 0.01
steps = 0
while var == 1:
	val = 0.0
	steps = steps +  1
	U2 = [[0.0 for x in range(m)] for y in range(n)] 
	# for i in range(n):
	# 	for j in range(m):
	# 		print '%.3f' % float(U[i][j]) ,
	# 	print 
	# print "----------------------------------------"
	for i in range(n):
		for j in range(m):
			mx = -inf
			if (i,j) in setE : 
				U2[i][j] = U[i][j]
				continue
			if (i,j) in setW :
				continue
			u = float(U[i][j]) 
			d = float(U[i][j])
			e = float(U[i][j])
			w = float(U[i][j])
			if i == 0 or (i-1,j) in setW :
				u = U[i][j]
			else :
				u = U[i-1][j]
			
			if i == n-1 or (i+1,j) in setW :
				d = U[i][j]
			else :
				d = U[i-1][j]
			
			if j == 0 or (i,j-1) in setW :
				w = U[i][j]
			else :
				w = U[i][j-1]
			
			if j == m-1 or (i-1,j+1) in setW :
				e = U[i][j]
			else :
				e = U[i][j+1]

			u = dis*u
			d = dis*d
			w = dis*w
			e = dis*e
			mx = max(mx,reward+0.8*u+0.1*(w+e))
			mx = max(mx,reward+0.8*d+0.1*(w+e))
			mx = max(mx,reward+0.8*e+0.1*(d+u))
			mx = max(mx,reward+0.8*w+0.1*(d+u))
			U2[i][j] = mx
			val = max(val,abso(U[i][j]-U2[i][j]))

	U = U2
	if val < error :
		break

for i in range(n):
	for j in range(m):
		print '%.3f' % float(U[i][j]) ,
	print 

print "Steps taken - " 
print steps