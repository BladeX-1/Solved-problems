#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Equivalent to your try-except block for environment checking
    ifstream flag_file("__localsystemflag__");
    if (flag_file.is_open()) {
        flag_file.close();
        // Redirect standard input to read from inp.txt
        freopen("inp.txt", "r", stdin);
    }

    int n, x;
    if (!(cin >> n >> x)) return 0;

    vector<int> weights(n);
    for (int i = 0; i < n; i++) {
        cin >> weights[i];
    }

    // Sort the weights (O(N log N))
    sort(weights.begin(), weights.end());

    int left = 0;
    int right = n - 1;
    int count = 0;

    // Two-pointer approach replaces the bisect + del logic
    while (left <= right) {
        // If the lightest and heaviest can pair up, move the left pointer
        if (weights[left] + weights[right] <= x) {
            left++;
        }
        
        // The heaviest item always gets packaged (either paired or alone)
        right--;
        count++;
    }

    cout << count << "\n";

    return 0;
}