class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        from collections import defaultdict as dd
        adj = dd(list)
        for a,b,p in flights:
            adj[a].append((b,p))

        ans = graph_bfs(adj,src,dst,k)
        if ans == float('inf'):
            return -1
        return ans

def graph_bfs(adj, start, end, k):
    import heapq
    poppedFromQue = set()
    q = [(0,0,start)]

    ans = float('inf')
    while q:
        topPrice,i,top = heapq.heappop(q)
        assert top!=end
        if i==k+1:
            continue
        if top in poppedFromQue: # already have smaller
            continue
        poppedFromQue.add(top)

        for (near,nearPrice) in adj[top]:
            if near in poppedFromQue:
                continue
            if near == end:
                ans = min(ans,topPrice+nearPrice)
                continue
            heapq.heappush(q,(topPrice+nearPrice,i+1,near))
    
    return ans


solution = Solution()
n = 5
flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
src = 0
dst = 2
k = 2
ans = solution.findCheapestPrice(n,flights,src,dst,k)
print(ans)