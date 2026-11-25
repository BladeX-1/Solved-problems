#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    // Optimize standard I/O operations for competitive programming
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<string> grid(n);
    queue<pair<int, int>> mq;
    
    // Store minimum time for a monster to reach each cell
    vector<vector<int>> distM(n, vector<int>(m, 1e9));

    int start_y = -1, start_x = -1;

    for (int i = 0; i < n; ++i) {
        cin >> grid[i];
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == 'M') {
                mq.push({i, j});
                distM[i][j] = 0;
            } else if (grid[i][j] == 'A') {
                start_y = i;
                start_x = j;
            }
        }
    }

    // Directions mapped to indices: 0=Up, 1=Down, 2=Left, 3=Right
    int dy[] = {-1, 1, 0, 0};
    int dx[] = {0, 0, -1, 1};
    char dir_char[] = {'U', 'D', 'L', 'R'};

    // 1. Multi-source BFS to find the shortest path from any monster to all cells
    while (!mq.empty()) {
        auto [y, x] = mq.front();
        mq.pop();

        for (int i = 0; i < 4; ++i) {
            int ny = y + dy[i];
            int nx = x + dx[i];

            if (ny >= 0 && ny < n && nx >= 0 && nx < m && grid[ny][nx] != '#') {
                if (distM[y][x] + 1 < distM[ny][nx]) {
                    distM[ny][nx] = distM[y][x] + 1;
                    mq.push({ny, nx});
                }
            }
        }
    }

    // 2. BFS for 'A' to find the exit
    queue<pair<int, int>> aq;
    vector<vector<int>> distA(n, vector<int>(m, 1e9));
    vector<vector<int>> parent(n, vector<int>(m, -1));

    aq.push({start_y, start_x});
    distA[start_y][start_x] = 0;

    int end_y = -1, end_x = -1;

    while (!aq.empty()) {
        auto [y, x] = aq.front();
        aq.pop();

        // Check if we reached the boundary
        if (y == 0 || y == n - 1 || x == 0 || x == m - 1) {
            end_y = y;
            end_x = x;
            break;
        }

        for (int i = 0; i < 4; ++i) {
            int ny = y + dy[i];
            int nx = x + dx[i];

            if (ny >= 0 && ny < n && nx >= 0 && nx < m && grid[ny][nx] != '#') {
                // 'A' can only move if it gets there strictly faster than any monster
                if (distA[y][x] + 1 < distA[ny][nx] && distA[y][x] + 1 < distM[ny][nx]) {
                    distA[ny][nx] = distA[y][x] + 1;
                    parent[ny][nx] = i; // Store the direction index used to get here
                    aq.push({ny, nx});
                }
            }
        }
    }

    // 3. Output results and re-construct the path
    if (end_y != -1) {
        cout << "YES\n";
        string path = "";
        int curr_y = end_y, curr_x = end_x;
        
        // Backtrack to build the directions string
        while (curr_y != start_y || curr_x != start_x) {
            int p = parent[curr_y][curr_x];
            path += dir_char[p];
            // Reverse the direction to move backward
            curr_y -= dy[p];
            curr_x -= dx[p];
        }
        
        // Since we traced from end to start, reverse to get chronological path
        reverse(path.begin(), path.end());
        
        cout << path.length() << "\n";
        cout << path << "\n";
    } else {
        cout << "NO\n";
    }

    return 0;
}