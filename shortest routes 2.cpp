#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#include <unordered_map>

using namespace std;

const long long INF = 1e18; // Equivalent to float('inf')

// Equivalent to graph_bfs
vector<long long> graph_bfs(int start, int n, const vector<unordered_map<int, long long>>& adj) {
    vector<long long> distances(n, INF);
    vector<bool> popped(n, false);
    int popped_count = 0;
    
    // Min-heap storing {distance, node}
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    
    // FIX: Changed from hardcoded distances[0] = 0 to distances[start] = 0
    distances[start] = 0;
    pq.push({0, start});
    
    while (!pq.empty()) {
        long long topDis = pq.top().first;
        int top = pq.top().second;
        pq.pop();
        
        if (popped[top]) continue;
        
        popped[top] = true;
        popped_count++;
        
        // Early exit: if all nodes are popped, we can stop
        if (popped_count == n) break;
        
        for (const auto& edge : adj[top]) {
            int near = edge.first;
            long long nearDis = edge.second;
            
            if (popped[near]) continue;
            
            if (distances[near] > nearDis + topDis) {
                distances[near] = nearDis + topDis;
                pq.push({distances[near], near});
            }
        }
    }
    
    // Convert unreachable nodes to -1
    for (int i = 0; i < n; ++i) {
        if (distances[i] == INF) {
            distances[i] = -1;
        }
    }
    
    return distances;
}

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Mimic the __localsystemflag__ try/except block
    ifstream flagFile("__localsystemflag__");
    if (flagFile.good()) {
        flagFile.close();
        freopen("inp.txt", "r", stdin);
    }

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    // Mimic defaultdict of defaultdict using a vector of unordered_maps
    // This allows us to handle multiple edges by taking the minimum weight
    vector<unordered_map<int, long long>> adj(n);
    
    for (int i = 0; i < m; ++i) {
        int a, b;
        long long w;
        cin >> a >> b >> w;
        a--; b--; // Convert to 0-based indexing
        
        if (adj[a].count(b)) {
            adj[a][b] = min(w, adj[a][b]);
            adj[b][a] = min(w, adj[b][a]);
        } else {
            adj[a][b] = w;
            adj[b][a] = w;
        }
    }

    // Precompute All-Pairs Shortest Path
    vector<vector<long long>> allPairDistance(n);
    for (int i = 0; i < n; ++i) {
        allPairDistance[i] = graph_bfs(i, n, adj);
        // cout << i << "\n"; // Kept this commented as it was printing 'i' in your python code
    }

    // Gather and print answers
    for (int i = 0; i < q; ++i) {
        int a, b;
        cin >> a >> b;
        cout << allPairDistance[a - 1][b - 1] << "\n";
    }

    return 0;
}