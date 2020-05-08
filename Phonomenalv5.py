
io = input().split()
numRes = int(io[0])
numPho = int(io[1])

map = {}

pho = input().split()
for x in range(numPho):
    pho[x] = int(pho[x])
path = []
for x in range(numRes-1):
    path.append(input().split())

for x in range(len(path)):
    for y in range(len(path[x])):
        path[x][y] = int(path[x][y])

map = {}

for m in range(numRes):
    map[m] = []

for p in path:
    map[p[0]].append(p[1])
    map[p[1]].append(p[0])

def hasPho(inp):
    ans = []
    for x in inp:
        if x in pho:
            ans.append(x)
    return ans
        
def areDifferent(l1, l2):
    ans = True

    for x in l1:
        if x in l2:
            ans = False
            break
    return ans
    

def theyConnectTo(burger):
    ans = []
    for x in burger:
        ans.extend(map[x])

    return ans

def closestPho(node,dont):
    li = [[node]]
    gt = [node]
    ans = []
    hasFound = False

    while not hasFound:
        l2 = []
        for e in li[len(li)-1]:
            l2.extend(list(filter(lambda z: not z in gt and not z in l2, theyConnectTo(li[len(li)-1]))))

        if len(list(filter(lambda t: t in pho and not t in dont, l2))) > 0:
            hasFound = True
        li.append(l2)
        gt.extend(l2)

    ans = list(filter(lambda u: u in pho and u not in dont, li[len(li)-1]))
    return [ans[0],len(li)-1]
                  
find = []

for p in pho:
    goneTo = [p]
    dist = 0
    while len(goneTo) < numPho:
        
        pie = closestPho(goneTo[len(goneTo)-1],goneTo)
        goneTo.append(pie[0])
        dist += pie[1]

    find.append(dist)

print(min(find))
