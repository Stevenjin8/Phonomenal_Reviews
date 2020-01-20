class Node:
    #the node class
    def __init__(self, value, is_pho):
        self.connections = []
        self.value = value
        self.is_pho = is_pho
        self.is_alive = True
        
    def connect(self,other):
        #connects to another node
        self.connections.append(other)
        other.connections.append(self)
        
    def cut(self):
        #cuts all connections with other nodes
        for node in self.connections:
            node.connections.remove(self)
            self.connections = []
    
    def is_leaf(self):
        #checks if a node is a leaf
        return len(self.connections) == 1
    
#input
nm = input().split(' ')
n = int(nm[0])
m = int(nm[1])
pho_restaurants = [int(x) for x in input().split(' ')]

#creates nodes
nodes = [Node(i, True) if i in pho_restaurants else Node(i, False) for i in range(n)]

#connects the nodes
for _ in range(n-1):
    connection = input().split(' ')
    nodes[int(connection[0])].connect(nodes[int(connection[1])])

def trim1():
    #cuts all non-pho leaves
    #note that it only cuts the connection way
    for node in nodes:
        if node.is_alive and node.is_leaf() and not node.is_pho:
            node.cut()
            node.is_alive = False
            #nodes.remove(node)
            
            
def done_trim1():
    #checks if trim1 will do anything
    for node in nodes:
        if node.is_alive and not node.is_pho and node.is_leaf():
            return False
    return True

def trim2():
    #removes all leaves
    to_remove = []
    for i, node in enumerate(nodes):
        if node.is_leaf() and node.is_alive:
            to_remove.append(i)
            node.cut()
            node.is_alive = False

#does the first trim phase
while not done_trim1():
    trim1()

#finds the total amount of nodes left
new_n = sum(node.is_alive for node in nodes)
max_dist = 0

#finds the greatest distance between two nodes by removing leaves until there are <= 2 nodes left
while sum(node.is_alive for node in nodes) > 2:
    trim2()
    max_dist += 2
if sum(node.is_alive for node in nodes) == 2:
    max_dist += 1

#prints
print( 2*((new_n-1)-max_dist) + max_dist)