#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// Use long long for distances to prevent overflow
typedef long long ll;

int main() {
    // 1. Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Python's environment check equivalent
#ifndef ONLINE_JUDGE
    // freopen("inp.txt", "r", stdin); // Uncomment to read from inp.txt locally
#endif

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    // Adjacency list: adj[u] stores pairs of {weight, v}
    vector<vector<pair<ll, int>>> adj(n);

    for (int i = 0; i < m; ++i) {
        int a, b;
        ll w;
        cin >> a >> b >> w;
        
        // 0-based indexing
        a--; b--; 
        adj[a].push_back({w, b});
    }

    // 2. Min-heap for Dijkstra: stores {cost, node}
    // greater<> ensures the smallest cost stays at the top
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> q;
    
    vector<int> popped(n, 0);
    vector<ll> ans;

    int start = 0;
    int end = n - 1;
    
    q.push({0LL, start});

    // 3. graph_bfs logic
    while (!q.empty()) {
        ll topPrice = q.top().first;
        int top = q.top().second;
        q.pop();

        popped[top]++;

        if (top == end) {
            ans.push_back(topPrice);
            if (ans.size() == k) {
                break;
            }
        }
        
        // Minor optimization: prevent processing a node if we've already 
        // finalized its k shortest paths
        if (popped[top] > k) continue; 

        for (auto& edge : adj[top]) {
            ll nearPrice = edge.first;
            int near = edge.second;

            if (popped[near] >= k) {
                continue;
            }
            
            q.push({topPrice + nearPrice, near});
        }
    }

    // 4. Output results
    for (int i = 0; i < ans.size(); ++i) {
        cout << ans[i] << (i == ans.size() - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}