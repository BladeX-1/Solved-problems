#include <iostream>
#include <vector>
#include <bitset>
#include <algorithm>

using namespace std;

// Set this to the maximum possible value of 'N' for the bitset.
// 50005 is a common constraint for O(V^2/64) bitset reachability problems.
const int MAXN = 50005; 

void topo(int i, const vector<vector<int>>& adj, vector<bool>& visited, vector<int>& revTopo) {
    visited[i] = true;
    for (int near : adj[i]) {
        if (!visited[near]) {
            topo(near, adj, visited, revTopo);
        }
    }
    revTopo.push_back(i);
}

void graph_dfs(int i, const vector<vector<int>>& adj, vector<bool>& visited, vector<bitset<MAXN>>& myReach) {
    visited[i] = true;
    for (int near : adj[i]) {
        if (visited[near]) {
            myReach[i] |= myReach[near];
            continue;
        }
        graph_dfs(near, adj, visited, myReach);
        myReach[i] |= myReach[near];
    }
    // Equivalent to myReach[i] |= (1 << i) in Python
    myReach[i].set(i); 
}

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Equivalent to the __localsystemflag__ check
#ifndef ONLINE_JUDGE
    if (FILE* file = freopen("inp.txt", "r", stdin)) {
        // Successfully opened local file
    }
#endif

    int n, v;
    if (!(cin >> n >> v)) return 0;

    vector<vector<int>> adj(n);
    for (int i = 0; i < v; ++i) {
        int a, b;
        cin >> a >> b;
        adj[a - 1].push_back(b - 1);
    }

    vector<bool> visited(n, false);
    vector<int> revTopo;

    // 1. Topological Sort
    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            topo(i, adj, visited, revTopo);
        }
    }

    // 2. Compute Reachability
    // Reset visited array
    fill(visited.begin(), visited.end(), false);
    vector<bitset<MAXN>> myReach(n);
    
    // reversed(reversed(revTopo)) is just revTopo forward
    for (int i : revTopo) {
        if (!visited[i]) {
            graph_dfs(i, adj, visited, myReach);
        }
    }

    // 3. Output the population count (bit_count)
    for (int i = 0; i < n; ++i) {
        cout << myReach[i].count() << (i == n - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}