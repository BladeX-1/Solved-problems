#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// Struct to hold our queue data cleanly
struct Node {
    int y;
    int x;
    int count;
};

vector<vector<int>> grid_bfs(int n) {
    // Initialize an n x n grid with -1
    vector<vector<int>> grid(n, vector<int>(n, -1));
    
    // 2D boolean array for visited tracking is much faster than a hash set in C++
    vector<vector<bool>> visited(n, vector<bool>(n, false));

    int dx[8] = {2, 1, -2, -1, 1, -2, -1, 2};
    int dy[8] = {1, 2, -1, -2, -2, 1, 2, -1};

    // std::queue is the C++ equivalent of Python's collections.deque
    queue<Node> q;
    
    q.push({0, 0, 0});
    visited[0][0] = true;

    while (!q.empty()) {
        Node current = q.front();
        q.pop();

        int topY = current.y;
        int topX = current.x;
        int topCount = current.count;

        grid[topY][topX] = topCount;

        for (int i = 0; i < 8; ++i) {
            int ynew = topY + dy[i];
            int xnew = topX + dx[i];

            // Inlined bounds check
            if (ynew >= 0 && ynew < n && xnew >= 0 && xnew < n) {
                if (!visited[ynew][xnew]) {
                    visited[ynew][xnew] = true;
                    q.push({ynew, xnew, topCount + 1});
                }
            }
        }
    }

    return grid;
}

int main() {
    int n = 8; // Default value mimicking `input() or 8`
    
    if (cin >> n) {
        // Successfully read n from standard input
    }

    vector<vector<int>> grid = grid_bfs(n);

    // Print the grid
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cout << grid[i][j] << (j == n - 1 ? "" : " ");
        }
        cout << "\n";
    }

    return 0;
}