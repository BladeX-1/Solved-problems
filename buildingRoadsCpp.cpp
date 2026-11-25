#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#include <chrono>

using namespace std;

// DFS is defined here to match your Python script, though it is unused in the main logic.
void graph_dfs(const vector<vector<int>>& adj, int i, vector<bool>& visited) {
    for (int near : adj[i]) {
        if (visited[near]) continue;
        visited[near] = true;
        graph_dfs(adj, near, visited);
    }
}

void graph_bfs(const vector<vector<int>>& adj, int start, vector<bool>& visited, vector<int>& cluster) {
    queue<int> q;
    q.push(start);
    visited[start] = true;
    cluster.push_back(start); // Keep track of elements in this component

    while (!q.empty()) {
        int top = q.front();
        q.pop();

        for (int near : adj[top]) {
            if (visited[near]) continue;
            visited[near] = true;
            q.push(near);
            cluster.push_back(near);
        }
    }
}

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Environment check
    ifstream flagFile("__localsystemflag__");
    bool isLocal = flagFile.good();
    flagFile.close();

    ifstream inpFile;
    if (isLocal) {
        inpFile.open("inp.txt");
        if (inpFile.is_open()) {
            // Redirect cin to read directly from the file
            cin.rdbuf(inpFile.rdbuf());
        }
    }

    int cities, roads;
    if (!(cin >> cities >> roads)) return 0;

    // 1-indexed adjacency list
    vector<vector<int>> adj(cities + 1);
    for (int i = 0; i < roads; ++i) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    int components = 0;
    // Using a boolean vector is O(1) for lookups and much faster than Python's set
    vector<bool> visitedGlobal(cities + 1, false);
    vector<vector<int>> clusters;

    auto start_time = chrono::high_resolution_clock::now();

    for (int i = 1; i <= cities; ++i) {
        if (visitedGlobal[i]) continue;
        components++;
        
        vector<int> cluster;
        graph_bfs(adj, i, visitedGlobal, cluster);
        clusters.push_back(cluster);
    }

    // Output edges to connect the components
    cout << components - 1 << "\n";
    for (size_t i = 0; i + 1 < clusters.size(); ++i) {
        // [0] replicates grabbing the first arbitrarily accessed element from the Python set
        cout << clusters[i][0] << " " << clusters[i + 1][0] << "\n"; 
    }

    if (isLocal) {
        auto end_time = chrono::high_resolution_clock::now();
        chrono::duration<double> diff = end_time - start_time;
        cout << diff.count() << "\n";
    }

    return 0;
}