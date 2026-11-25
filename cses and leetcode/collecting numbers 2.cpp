#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    // Fast I/O for competitive programming
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> arr(n);
    vector<int> pos(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
        arr[i]--; // 0-based indexing (like lambda x: x-1)
        pos[arr[i]] = i;
    }

    // Calculate initial rounds
    int round = 1;
    for (int i = 1; i < n; ++i) {
        if (pos[i] < pos[i - 1]) {
            round++;
        }
    }

    // Process m queries
    for (int k = 0; k < m; ++k) {
        int a, b;
        cin >> a >> b;
        a--; b--; // Convert to 0-based index

        if (a == b) {
            cout << round << (k == m - 1 ? "" : " ");
            continue;
        }

        int i = arr[a];
        int j = arr[b];

        // Gather all boundaries that might have an inversion change
        vector<int> check = {i - 1, i, j - 1, j};
        sort(check.begin(), check.end());
        // Remove duplicate checks to handle adjacent elements (i == j +/- 1)
        check.erase(unique(check.begin(), check.end()), check.end());

        int previous = 0;
        for (int idx : check) {
            if (idx >= 0 && idx < n - 1) {
                if (pos[idx] > pos[idx + 1]) {
                    previous++;
                }
            }
        }

        // Apply swap
        swap(pos[i], pos[j]);
        swap(arr[a], arr[b]);

        int later = 0;
        for (int idx : check) {
            if (idx >= 0 && idx < n - 1) {
                if (pos[idx] > pos[idx + 1]) {
                    later++;
                }
            }
        }

        // Update total round count based on delta
        round += (later - previous);
        
        cout << round << (k == m - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}