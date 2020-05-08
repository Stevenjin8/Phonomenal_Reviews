numRes = 8
numPho = 5
pho = [4, 0, 3, 6, 7]
path = [[0, 1],[0, 2],[2, 3],[3, 4],[3, 7],[1, 5],[1, 6]]

map = {}

for m in range(numRes):
    map[m] = []

for p in path:
    map[p[0]].append(p[1])
    map[p[1]].append(p[0])
"""
def hasPho(inp):
    return list(filter(lambda y: y in pho, inp))

def hasPhoMult(fries):
    ans = []
    for x in fries:
        ans.extend(list(filter(lambda c: not c in ans, hasPho(x))))
    return ans
"""

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
    print(len(li)-1, ans[0])
    return ans[0]

friedChicken = []

def closestPhoDist(node,dont):
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

    return len(li)-1

                   
find = []


for p in pho:
    goneTo = [p]
    dist = 0
    while len(goneTo) < numPho:
        lgt = len(goneTo)
        goneTo.append(closestPho(goneTo[lgt-1],goneTo))
        'dist += closestPhoDist(goneTo[lgt-1],goneTo)'
    friedChicken.append(goneTo)
    find.append(dist)

