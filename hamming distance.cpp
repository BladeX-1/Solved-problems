#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Equivalent to your local system flag check
    // If you compile locally with -DONLINE_JUDGE, this is skipped.
    // Otherwise, it reads from inp.txt just like your Python script.
#ifndef ONLINE_JUDGE
    if (freopen("inp.txt", "r", stdin) == NULL) {
        // File not found, gracefully fall back to standard input
    }
#endif

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<unsigned long long> numbers(n);
    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        // Convert binary string to unsigned long long (base 2)
        numbers[i] = stoull(s, nullptr, 2);
    }

    int ans = k;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            // XOR the numbers and count the set bits (1s)
            unsigned long long xor_val = numbers[i] ^ numbers[j];
            int temp = __builtin_popcountll(xor_val); 
            
            if (temp < ans) {
                ans = temp;
            }
        }
    }

    cout << ans << "\n";

    return 0;
}