#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Direction arrays (Down, Right, Up, Left)
const int dx[] = {0, 1, 0, -1};
const int dy[] = {1, 0, -1, 0};
const char dz[] = {'D', 'R', 'U', 'L'};

int total_count = 0;
bool grid[7][7] = {false};
string s;
int s_len;

inline bool isBounded(int y, int x) {
    return 0 <= y && y < 7 && 0 <= x && x < 7;
}

void grid_dfs(int y, int x, int si) {
    if (x == 0 && y == 6 && si == s_len) {
        total_count++;
        return;
    } else if ((x == 0 && y == 6) || si == s_len) {
        return;
    }

    for (int i = 0; i < 4; i++) {
        // Skip directions that don't match the required step (unless it's '?')
        if (s[si] != '?' && s[si] != dz[i]) {
            continue;
        }

        int ynew = y + dy[i];
        int xnew = x + dx[i];
        char d = dz[i];

        if (!isBounded(ynew, xnew)) continue;
        if (grid[ynew][xnew]) continue;

        // Pruning checks for Up
        if (d == 'U' &&
            (
                (
                    (ynew == 0 || grid[ynew - 1][xnew]) &&
                    (xnew == 0 || xnew == 6 || (!grid[ynew][xnew - 1] && !grid[ynew][xnew + 1]))
                ) ||
                (
                    ynew > 0 && xnew > 0 &&
                    grid[ynew - 1][xnew - 1] &&
                    !grid[ynew][xnew - 1] && !grid[ynew - 1][xnew]
                ) ||
                (
                    ynew > 0 && xnew != 6 &&
                    grid[ynew - 1][xnew + 1] &&
                    !grid[ynew][xnew + 1] && !grid[ynew - 1][xnew]
                )
            )) {
            continue;
        }

        // Pruning checks for Down
        if (d == 'D' &&
            (
                (
                    (ynew == 6 || grid[ynew + 1][xnew]) &&
                    xnew != 0 && xnew != 6 &&
                    !grid[ynew][xnew - 1] && !grid[ynew][xnew + 1]
                ) ||
                (
                    ynew + 1 < 7 && xnew - 1 >= 0 &&
                    grid[ynew + 1][xnew - 1] &&
                    !grid[ynew + 1][xnew] && !grid[ynew][xnew - 1]
                ) ||
                (
                    ynew + 1 < 7 && xnew + 1 < 7 &&
                    grid[ynew + 1][xnew + 1] &&
                    !grid[ynew + 1][xnew] && !grid[ynew][xnew + 1]
                )
            )) {
            continue;
        }

        // Pruning checks for Left
        if (d == 'L' &&
            (
                (
                    (xnew == 0 || grid[ynew][xnew - 1]) &&
                    ynew != 0 && ynew != 6 &&
                    !grid[ynew - 1][xnew] && !grid[ynew + 1][xnew]
                ) ||
                (
                    ynew - 1 >= 0 && xnew - 1 >= 0 &&
                    grid[ynew - 1][xnew - 1] &&
                    !grid[ynew - 1][xnew] && !grid[ynew][xnew - 1]
                ) ||
                (
                    ynew + 1 < 7 && xnew - 1 >= 0 &&
                    grid[ynew + 1][xnew - 1] &&
                    !grid[ynew + 1][xnew] && !grid[ynew][xnew - 1]
                )
            )) {
            continue;
        }

        // Pruning checks for Right
        if (d == 'R' &&
            (
                (
                    (xnew == 6 || grid[ynew][xnew + 1]) &&
                    ynew != 0 && ynew != 6 &&
                    !grid[ynew - 1][xnew] && !grid[ynew + 1][xnew]
                ) ||
                (
                    ynew - 1 >= 0 && xnew + 1 < 7 &&
                    grid[ynew - 1][xnew + 1] &&
                    !grid[ynew - 1][xnew] && !grid[ynew][xnew + 1]
                ) ||
                (
                    ynew + 1 < 7 && xnew + 1 < 7 &&
                    grid[ynew + 1][xnew + 1] &&
                    !grid[ynew + 1][xnew] && !grid[ynew][xnew + 1]
                )
            )) {
            continue;
        }

        // Recursion
        grid[ynew][xnew] = true;
        grid_dfs(ynew, xnew, si + 1);
        grid[ynew][xnew] = false;
    }
}

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (cin >> s) {
        s_len = s.length();
        grid[0][0] = true;
        
        grid_dfs(0, 0, 0);
        
        cout << total_count << "\n";
    }

    return 0;
}