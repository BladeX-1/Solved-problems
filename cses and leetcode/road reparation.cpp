#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Structure to represent an edge
struct Edge {
    int u, v;
    long long weight;
    
    // Sort edges based on weight
    bool operator<(const Edge& other) const {
        return weight < other.weight;
    }
};

// Disjoint Set Union (DSU) with Path Compression and Union by Size
struct DSU {
    vector<int> parent;
    vector<int> sz;
    
    DSU(int n) {
        parent.resize(n);
        sz.resize(n, 1);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }
    
    int find(int i) {
        if (parent[i] == i)
            return i;
        // Path compression
        return parent[i] = find(parent[i]);
    }
    
    bool unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        
        if (root_i != root_j) {
            // Union by size
            if (sz[root_i] < sz[root_j]) {
                swap(root_i, root_j);
            }
            parent[root_j] = root_i;
            sz[root_i] += sz[root_j];
            return true;
        }
        return false;
    }
};

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Edge> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].weight;
        // Convert to 0-indexed
        edges[i].u--;
        edges[i].v--;
    }

    // Sorting edges is generally faster than using a priority queue in C++ for Kruskal's
    sort(edges.begin(), edges.end());

    DSU dsu(n);
    long long ans = 0;
    int edges_used = 0;

    // Kruskal's Algorithm
    for (const auto& edge : edges) {
        if (dsu.unite(edge.u, edge.v)) {
            ans += edge.weight;
            edges_used++;
        }
    }

    // A spanning tree on N vertices must have exactly N-1 edges
    if (edges_used != n - 1) {
        cout << "IMPOSSIBLE\n";
    } else {
        cout << ans << "\n";
    }

    return 0;
}