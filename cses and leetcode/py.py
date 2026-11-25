# from os import *
# from sys import *
# from collections import *
# from math import *

from collections import defaultdict as dd

def shortestAlternatingPath(nodeCount, red, green, redEdges, greenEdges):
    adj0 = dd(list)
    for a,b in redEdges:
        adj0[a].append(b)
    
    adj1 = dd(list)
    for a,b in greenEdges:
        adj1[a].append(b)

    return graph_bfs(0,adj0,adj1,nodeCount)    





class Helper:
    def __init__(self,node,lastEdgeColor):
        self.node = node
        self.lastEdgeColor = lastEdgeColor

def graph_bfs(i,adj0,adj1,n): 
    # def graph_bfs(grid,y,x): 
    edgeTraversed = set() 

    q = [Helper(node=i,lastEdgeColor=None),Helper(None,None)]
    allDistance = [float('inf')]*n
    dis = 0

    while len(q)>1: 
        # print(len(q))
        topElement = q.pop(0)
        top = topElement.node
        lastEdgeColor = topElement.lastEdgeColor

        if top == None:
            dis+=1
            NoneValue = topElement
            q.append(NoneValue)
            continue
        
        allDistance[top] = min(allDistance[top], dis)

        if lastEdgeColor!=1:
            adj = adj1
            selfColor = 1
            for near in adj[top]: 
    
                if (top,near,selfColor) in edgeTraversed: 
                    continue 
    
                edgeTraversed.add((top,near,selfColor))
                q.append(Helper(node=near,lastEdgeColor=1)) 
        if lastEdgeColor!=0:
            adj = adj0
            selfColor = 0
            for near in adj[top]: 
    
                if (top,near,selfColor) in edgeTraversed: 
                    continue 
    
                edgeTraversed.add((top,near,selfColor))
                q.append(Helper(node=near,lastEdgeColor=0)) 
    return allDistance


f = open("inp.txt", "r")

t = int(f.readline().strip())
for _ in range(t):
    if _==1:
        pass
    n,r,g = [*map(int,f.readline().strip().split(' '))]
    redEdges = []
    for _ in range(r):
        a,b = [*map(int,f.readline().strip().split(' '))]
        redEdges.append((a,b))
    greenEdges = []
    for _ in range(g):
        a,b = [*map(int,f.readline().strip().split(' '))]
        greenEdges.append((a,b))
    print(shortestAlternatingPath(n, r, g, redEdges, greenEdges))
