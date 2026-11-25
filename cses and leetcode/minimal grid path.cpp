#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct Point {
    int y, x;
};

string grid_bfs(const vector<string>& grid, int n) {
    // 2D visited array initialization
    vector<vector<bool>> visited(n, vector<bool>(n, false));

    int dy[] = {1, 0};
    int dx[] = {0, 1};

    // Use simple, clean layer vectors instead of manual deque popping
    vector<Point> curr_layer;
    curr_layer.push_back({0, 0});
    visited[0][0] = true;

    string ans = "";
    ans += grid[0][0]; // Start string with the top-left character

    // Construct the rest of the 2n - 2 steps
    for (int step = 0; step < 2 * n - 2; ++step) {
        char lowest = 'Z' + 1; // Look for the absolute minimum char available

        // Phase 1: Scan all reachable neighbors across the ENTIRE layer to find the true global minimum
        for (const auto& p : curr_layer) {
            for (int i = 0; i < 2; ++i) {
                int ynew = p.y + dy[i];
                int xnew = p.x + dx[i];

                if (ynew >= n || xnew >= n) continue; // Out of bounds
                if (visited[ynew][xnew]) continue;

                if (grid[ynew][xnew] < lowest) {
                    lowest = grid[ynew][xnew];
                }
            }
        }

        ans += lowest;
        vector<Point> next_layer;

        // Phase 2: Collect only the coordinates that match our true global minimum
        for (const auto& p : curr_layer) {
            for (int i = 0; i < 2; ++i) {
                int ynew = p.y + dy[i];
                int xnew = p.x + dx[i];

                if (ynew >= n || xnew >= n) continue;
                if (visited[ynew][xnew]) continue;

                if (grid[ynew][xnew] == lowest) {
                    visited[ynew][xnew] = true;
                    next_layer.push_back({ynew, xnew});
                }
            }
        }

        curr_layer = move(next_layer); // Shift to the next layer seamlessly
    }

    return ans;
}

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<string> grid(n);
    for (int i = 0; i < n; ++i) {
        cin >> grid[i];
    }

    cout << grid_bfs(grid, n) << "\n";

    return 0;
}
