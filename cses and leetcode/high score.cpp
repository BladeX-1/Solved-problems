#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e17;

// BFS function matching your graph_bfs logic exactly
void graph_bfs(const vector<vector<int>>& graph, int start, vector<bool>& addedToQue) {
    queue<int> q;
    q.push(start);
    addedToQue[start] = true;
    
    while (!q.empty()) {
        int top = q.front();
        q.pop();
        
        for (int near : graph[top]) {
            if (addedToQue[near]) {
                continue;
            }
            addedToQue[near] = true;
            q.push(near);
        }
    }
}

int main() {
    // Local environment check (matches your try-except block)
    #ifndef ONLINE_JUDGE
    if (freopen("inp.txt", "r", stdin) == nullptr) {
        // Fallback to std input if file is missing
    }
    #endif

    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, edges_count;
    if (!(cin >> n >> edges_count)) return 0;

    // Use a map to handle multiple edges correctly (keeps the min weight)
    map<pair<int, int>, long long> edge_map;
    vector<vector<int>> revAdj(n);

    for (int i = 0; i < edges_count; ++i) {
        int a, b;
        long long w;
        cin >> a >> b >> w;
        a--; b--; // 0-based indexing
        
        pair<int, int> edge = {a, b};
        if (edge_map.find(edge) == edge_map.end()) {
            edge_map[edge] = -w;
        } else {
            edge_map[edge] = min(edge_map[edge], -w);
        }
        
        revAdj[b].push_back(a);
    }

    // Build the adjacency list and edge list for Bellman-Ford
    vector<vector<int>> adj(n);
    struct Edge { int u, v; long long w; };
    vector<Edge> edge_list;
    
    for (auto const& [nodes, weight] : edge_map) {
        adj[nodes.first].push_back(nodes.second);
        edge_list.push_back({nodes.first, nodes.second, weight});
    }

    // Bellman Ford
    vector<long long> distances(n, INF);
    distances[0] = 0;
    
    vector<bool> cycles(n, false);
    bool has_cycle = false;

    for (int i = 0; i < n; ++i) {
        for (const auto& edge : edge_list) {
            int a = edge.u;
            int b = edge.v;
            long long w = edge.w;

            if (distances[a] != INF && distances[b] > distances[a] + w) {
                if (i == n - 1) {
                    cycles[b] = true;
                    has_cycle = true;
                }
                distances[b] = distances[a] + w;
            }
        }
    }

    bool common = false;

    if (has_cycle) {
        vector<bool> allFromStart(n, false);
        graph_bfs(adj, 0, allFromStart);

        vector<bool> fromAllToEnd(n, false);
        graph_bfs(revAdj, n - 1, fromAllToEnd);

        // Intersection (allFromStart & fromAllToEnd & cycles)
        for (int i = 0; i < n; ++i) {
            if (allFromStart[i] && fromAllToEnd[i] && cycles[i]) {
                common = true;
                break;
            }
        }
    }

    if (common) {
        cout << -1 << "\n";
    } else {
        cout << -distances[n - 1] << "\n";
    }

    return 0;
}