#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <fstream>
#include <algorithm> // For std::reverse

using namespace std;

string grid_bfs(const vector<string>& grid, int startY, int startX) {
    int ylen = grid.size();
    int xlen = grid[0].size();

    vector<vector<bool>> visited(ylen, vector<bool>(xlen, false));
    // Store the direction index (0, 1, 2, or 3) used to reach a cell
    vector<vector<int>> parent_dir(ylen, vector<int>(xlen, -1));

    int dx[] = {0, 1, 0, -1};
    int dy[] = {1, 0, -1, 0};
    char dd[] = {'D', 'R', 'U', 'L'};

    queue<pair<int, int>> q;
    q.push({startY, startX});
    visited[startY][startX] = true;

    int endY = -1, endX = -1;

    while (!q.empty()) {
        int topY = q.front().first;
        int topX = q.front().second;
        q.pop();

        for (int i = 0; i < 4; ++i) {
            int ynew = topY + dy[i];
            int xnew = topX + dx[i];

            if (ynew < 0 || ynew >= ylen || xnew < 0 || xnew >= xlen) {
                continue;
            }
            if (visited[ynew][xnew] || grid[ynew][xnew] == '#') {
                continue;
            }

            visited[ynew][xnew] = true;
            parent_dir[ynew][xnew] = i; // Remember how we got here
            
            if (grid[ynew][xnew] == 'B') {
                endY = ynew;
                endX = xnew;
                // Empty the queue to exit early (or just break)
                while (!q.empty()) q.pop(); 
                break;
            }

            q.push({ynew, xnew});
        }
    }

    // If we never found 'B'
    if (endY == -1) {
        return "";
    }

    // Reconstruct the path by backtracking from 'B' to 'A'
    string path = "";
    int currY = endY;
    int currX = endX;

    while (currY != startY || currX != startX) {
        int p = parent_dir[currY][currX];
        path += dd[p];
        // Move backwards to the parent cell
        currY -= dy[p];
        currX -= dx[p];
    }

    // Since we traced from end to start, reverse the string at the end
    reverse(path.begin(), path.end());
    
    return path;
}

int main() {
    // Fast I/O is critical for competitive programming
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    ifstream flag_file("__localsystemflag__");
    if (flag_file.good()) {
        flag_file.close();
        freopen("inp.txt", "r", stdin);
    }

    int ylen, xlen;
    if (!(cin >> ylen >> xlen)) return 0;

    vector<string> grid(ylen);
    int startY = -1, startX = -1;

    for (int y = 0; y < ylen; ++y) {
        cin >> grid[y];
        for (int x = 0; x < xlen; ++x) {
            if (grid[y][x] == 'A') {
                startY = y;
                startX = x;
            }
        }
    }

    string ans = grid_bfs(grid, startY, startX);

    if (!ans.empty()) {
        cout << "YES\n";
        cout << ans.length() << "\n";
        cout << ans << "\n";
    } else {
        cout << "NO\n";
    }

    return 0;
}