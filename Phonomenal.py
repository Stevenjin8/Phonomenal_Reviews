nm = input().split(' ')
n = int(nm[0])
m = int(nm[1])
pho_restaurants = [int(x) for x in input().split(' ')]
graph = [[0 for x in range(n)] for x in range(n)]

zeroes = [0 for x in range(n)]
for x in range(n-1):
    vertex = [int(x) for x in input().split(' ')]
    graph[vertex[0]][vertex[1]] = 1
    graph[vertex[1]][vertex[0]] = 1

def bad_leaves():
    for i, x in enumerate(graph):
        if not i in pho_restaurants and x.count(1) == 1:
            return True
    return False

def is_dead():
    num = 0
    for l in graph:
        if l.count(1) > 1:
            return False
    return True

def trim():
    to_del=[]
    for y, row in enumerate(graph):
        if row.count(1) == 1:
            x = row.index(1)
            to_del.append([x,y])
    for i in to_del:
        graph[i[0]][i[1]] = 0
        graph[i[1]][i[0]] = 0

while bad_leaves():
    for x in range(n):
        if not x in pho_restaurants and graph[x].count(1) == 1:
            y = graph[x].index(1)
            graph[y][x] = 0
            graph[x][y] = 0
            
new_n = len([1 for x in graph if x != zeroes])

#maxes = [[-1 for x in range(n)] for x in range(n)]
max_dist = 0
while not is_dead():
    trim()
    max_dist += 2

num_left = 0

for l in graph:
    if 1 in l:
        num_left +=0.5
    if num_left 1:
        break
        
if num_left == 1:
    max_dist+=1

print( 2*((new_n-1)-max_dist) + max_dist)
