import queue

def root(p, v):
	if p[v] < 0:
		return v
	else:
		p[v] = root(p, p[v])
		return p[v]

def isSameSet(p, v, u):
	return root(p, v) == root(p, u)

def merge(p, v, u):
	v = root(p, v)
	u = root(p, u)
	if v == u:
		return

	if p[u] < p[v]:
		swap = p[u]
		p[u] = p[v]
		p[v] = swap

	p[v] += p[u]
	p[u] = v

stream = input().split()
nVertices = int(stream[0])
nEdges = int(stream[1])

edges = queue.PriorityQueue()
for e in range(nEdges):
	stream = input().split()
	v1 = int(stream[0])
	v2 = int(stream[1])
	weight = int(stream[2])

	edges.put((weight, v1, v2))

parents = [-1] * nVertices
usedEdges = queue.PriorityQueue()
unusedEdges = queue.PriorityQueue()
totalWeight = 0
while not edges.empty():
	edge = edges.get()
	if isSameSet(parents, edge[1], edge[2]):
		unusedEdges.put(edge)
	else:
		merge(parents, edge[1], edge[2])
		totalWeight += edge[0]
		usedEdges.put(edge)

print('First Spanning Tree Cost: {0}'.format(totalWeight))

for p in range(len(parents)):
	parents[p] = -1

edge = unusedEdges.get()
merge(parents, edge[1], edge[2])
totalWeight = edge[0]

while not usedEdges.empty():
	edge = usedEdges.get()
	if not isSameSet(parents, edge[1], edge[2]):
		merge(parents, edge[1], edge[2])
		totalWeight += edge[0]

print('Second Spanning Tree Cost: {0}'.format(totalWeight))
