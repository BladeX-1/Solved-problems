class Solution:
    def shortestPath(self,n, m, edges):
        from collections import defaultdict as dd
        adj = dd(list)
        for a,b,w in edges:
            adj[a-1].append((b-1,w))
            adj[b-1].append((a-1,w))
        
        return graph_bfs(adj,0,n-1,n)


def graph_bfs(adj, start, dst, n):
    import heapq

    popped = set()

    parent = [-1]*n
    q = [(0,start,-1)]
    ansDistance = -1
    while q:
        topDistance, top, topParent = heapq.heappop(q)
        if top in popped:
            continue
        popped.add(top)
        parent[top] = topParent
        if top==dst:
            ansDistance = topDistance
            break

        for near,nearDistance in adj[top]:
            if near in popped:
                continue
            heapq.heappush(q,(topDistance+nearDistance,near,top))
    
    if ansDistance == -1:
        return [-1]
    else:
        ans = []
        p = dst
        while(p!=-1):
            ans.append(p)
            p = parent[p]
        ans.reverse()
        return [ansDistance]+ans

solution = Solution()
edges = [[1,2,2], [2,5,5], [2,3,4], [1,4,1],[4,3,3],[3,5,1]] 
m = len(edges)
n = 5
print(solution.shortestPath(n,m,edges))