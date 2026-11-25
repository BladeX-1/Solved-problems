#include <iostream>
#include <vector>
#include <fstream>
#include <cassert>
#include <set>
#include <algorithm>

using namespace std;

// Backtracking function
bool bt(const vector<vector<int>>& adj, int i, int n, vector<int>& colors, 
        int& uniqueColors, vector<int>& counterColors, int& bestAns, 
        vector<vector<int>>& colorsAns, int maxColor) {
            
    if (i == n) {
        bestAns = uniqueColors;
        colorsAns.push_back(colors);
        return true;
    }
    
    for (int c = 0; c < bestAns; ++c) {
        bool works = true;
        for (int near : adj[i]) {
            if (colors[near] == c) {
                works = false;
                break;
            }
        }
        if (!works) continue;
        
        colors[i] = c;
        if (counterColors[c] == 0) uniqueColors++;
        counterColors[c]++;
        
        bool shouldBreak = false;
        if (uniqueColors > bestAns) {
            shouldBreak = true;
        }
        if (maxColor + 1 < c) {
            shouldBreak = true;
        }
        
        bool isSolved = false;
        if (!shouldBreak) {
            if (uniqueColors == bestAns && !colorsAns.empty()) {
                isSolved = false;
            } else {
                shouldBreak = false;
                isSolved = bt(adj, i + 1, n, colors, uniqueColors, counterColors, bestAns, colorsAns, max(maxColor, c));
            }
        } else {
            isSolved = false;
        }
        
        // Backtrack
        counterColors[c]--;
        if (counterColors[c] == 0) uniqueColors--;
        colors[i] = -1;
        
        if (isSolved && i == n - 1) {
            return true;
        }
        if (shouldBreak) {
            break;
        }
    }
    return false;
}

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Replicate Python's try-except file input logic
    ifstream local_flag("__localsystemflag__");
    if (local_flag.good()) {
        local_flag.close();
        if (freopen("inp.txt", "r", stdin) == nullptr) {
            cerr << "Failed to open inp.txt" << endl;
        }
    }

    int n, edges;
    if (!(cin >> n >> edges)) return 0;

    // Use set initially to deduplicate edges
    vector<set<int>> adjx(n);
    for (int k = 0; k < edges; ++k) {
        int a, b;
        cin >> a >> b;
        assert(a != b);
        adjx[a - 1].insert(b - 1);
        adjx[b - 1].insert(a - 1);
    }

    vector<vector<int>> adj(n);
    int fullyConnected = 0;
    int maxEdges = 0;
    
    for (int i = 0; i < n; ++i) {
        adj[i] = vector<int>(adjx[i].begin(), adjx[i].end());
        maxEdges = max(maxEdges, (int)adj[i].size());
        if (adj[i].size() == n - 1) {
            fullyConnected++;
        }
    }

    if (fullyConnected == n) {
        cout << n << "\n";
        for (int i = 1; i <= n; ++i) {
            cout << i << (i == n ? "" : " ");
        }
        cout << "\n";
        return 0;
    } else if (maxEdges == 0) {
        cout << 1 << "\n";
        for (int i = 1; i <= n; ++i) {
            cout << 1 << (i == n ? "" : " ");
        }
        cout << "\n";
        return 0;
    }

    vector<int> colors(n, -1);
    colors[0] = 0;
    vector<vector<int>> colorsAns;
    
    int bestAns = maxEdges + 1;
    vector<int> counterColors(n + 1, 0); 
    counterColors[0] = 1;
    int uniqueColors = 1;

    bt(adj, 1, n, colors, uniqueColors, counterColors, bestAns, colorsAns, 0);

    cout << bestAns << "\n";
    
    // Find and format the correct answer list matching `bestAns`
    for (size_t i = 0; i < colorsAns.size(); ++i) {
        const auto& current_colors = colorsAns[i];
        
        int u_colors = 0;
        vector<int> c_counts(n + 1, 0);
        for (int c : current_colors) {
            if (c_counts[c] == 0) u_colors++;
            c_counts[c]++;
        }
        
        if (u_colors == bestAns) {
            for (int j = 0; j < n; ++j) {
                // + 1 to convert from 0-indexed logic to 1-indexed output
                cout << current_colors[j] + 1 << (j == n - 1 ? "" : " ");
            }
            cout << "\n";
            break;
        }
    }

    return 0;
}