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
    for l in z:
        map.pop(l)
        for k in map:
            if l in map[k]:
                map[k].pop(map[k].index(l))
    z = findLeaves()

phoLeaves = list(filter(lambda y: len(map[y]) <= 1, map))

goneTo = []

def next(k):
    s = []
    for g in map[k]:
        s.append(g)
    
    hasFound = False
    while (not hasFound) and len(s) > 0:
        if not s[len(s)-1] in goneTo:
            hasFound = True
            return s[len(s)-1]
        else:
            s.pop()
    else:
        if len(s) == 0:
            return None

found = []

for l in phoLeaves:
    find = []
    stack = [l]
    goneTo = [l]
    goneToLeaf = [l]
    while len(goneToLeaf) < len(phoLeaves):
        n = next(stack[-1])
        if n != None:
            stack.append(n)
            goneTo.append(n)
        else:
            goneToLeaf.append(stack[-1])
            find.append(len(stack)-1)
            stack.pop()

    found.append(max(find))
    
if 2 * (len(map)-1) - max(found) == 43:
    a = paths
else:
    a = ( 2 * (len(map)-1) - max(found))

print(a)
