io = input().split()
numPho = int(io[1])
numRes = int(io[0])
pho = input().split()
for p in range(len(pho)):
    pho[p] = int(pho[p])

paths = []

for u in range(numRes-1):
    paths.append(input())

for u in range(len(paths)):
    paths[u] = paths[u].split()

for h in range(len(paths)):
    for y in range(2):
        paths[h][0] = int(paths[h][0])
        paths[h][1] = int(paths[h][1])

map = {}

for x in range(numRes):
    map[x] = []

for x in paths:
    map[x[1]].append(int(x[0]))
    map[x[0]].append(int(x[1]))

def findLeaves():
    return list(filter(lambda y: len(map[y]) <= 1 and not y in pho, map))

z = findLeaves()


while len(z) > 0:
    print(z)
    for l in z:
        map.pop(l)
        for k in map:
            if l in map[k]:
                map[k].pop(map[k].index(l))
    z = findLeaves()

phoLeaves = list(filter(lambda y: len(map[y]) <= 1, map))

goneTo = []
goTo = []
c= 0

for r in phoLeaves:
    goneTo = [r]
    counter = 0
    while not len(goneTo) == numPho:
        for i in goneTo:
            goneTo = goneTo + map[i]
        counter += 1
        goneTo = list(set(goneTo))
    if c < counter:
        c = counter
    
        
    
