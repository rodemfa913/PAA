class House:
	def __init__(self):
		self.distance = 0
		self.ways = []

class Way:
	def __init__(self):
		self.destination = None
		self.length = 1

t = int(input())

for case in range(1, t + 1):
	line = input().split()
	n = int(line[0])
	m = int(line[1])

	houses = []
	for vertex in range(n):
		houses.append(House())

	for edge in range(m):
		line = input().split()
		u = int(line[0])
		v = int(line[1])
		c = int(line[2])

		hu = houses[u - 1]
		hv = houses[v - 1]

		w = Way()
		hu.ways.append(w)
		w.destination = hv
		w.length = c

		w = Way()
		hv.ways.append(w)
		w.destination = hu
		w.length = c

	k = int(input())
	line = input().split()
	for request in range(k):
		h = houses[int(line[request]) - 1]
