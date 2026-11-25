#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool bt(const vector<string>& grid, vector<string>& gridAns, int y, int x, int ylen, int xlen) {
    // Base case: Reached the end of the grid
    if (y == ylen) {
        return true;
    }

    // Boolean array representing the set {"A", "B", "C", "D"}
    // true means available, false means removed
    bool possibles[4] = {true, true, true, true};

    // Remove top neighbor's character if it exists
    if (y != 0 && gridAns[y - 1][x] != '.') {
        possibles[gridAns[y - 1][x] - 'A'] = false;
    }
    
    // Remove left neighbor's character if it exists
    if (x != 0 && gridAns[y][x - 1] != '.') {
        possibles[gridAns[y][x - 1] - 'A'] = false;
    }
    
    // Remove the character present in the original grid
    if (grid[y][x] >= 'A' && grid[y][x] <= 'D') {
        possibles[grid[y][x] - 'A'] = false;
    }

    // Calculate next coordinates (Replaces getNextYX function)
    int ny = y, nx = x + 1;
    if (nx == xlen) {
        nx = 0;
        ny++;
    }

    // Try all available characters
    for (int i = 0; i < 4; ++i) {
        if (possibles[i]) {
            gridAns[y][x] = 'A' + i;
            
            if (bt(grid, gridAns, ny, nx, ylen, xlen)) {
                return true;
            }
            
            // Backtrack: Reset to placeholder
            gridAns[y][x] = '.'; 
        }
    }

    return false;
}

int main() {
    // Optimize standard I/O operations for competitive programming speed
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int ylen, xlen;
    if (!(cin >> ylen >> xlen)) return 0;

    vector<string> grid(ylen);
    for (int i = 0; i < ylen; ++i) {
        cin >> grid[i];
    }

    // Initialize answer grid with '.' acting as Python's `None`
    vector<string> gridAns(ylen, string(xlen, '.'));

    if (!bt(grid, gridAns, 0, 0, ylen, xlen)) {
        cout << "IMPOSSIBLE\n";
    } else {
        for (int i = 0; i < ylen; ++i) {
            cout << gridAns[i] << "\n";
        }
    }

    return 0;
}