#include <iostream>
#include <vector>

using namespace std;

// ceil(log2(10^7)) is 24, using 25 to be safe
const int BITS = 25; 

long long getNumFromWindow(const vector<int>& window) {
    long long ans = 0;
    for (int j = 0; j < BITS; ++j) {
        if (window[j] > 0) {
            ans |= (1LL << j);
        }
    }
    return ans;
}

int main() {
    // 1. FAST I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // 2. EQUIVALENT TO PYTHON LOCAL FILE CHECK
    // If you compile with -DONLINE_JUDGE, it reads from standard input.
    // Otherwise, it attempts to read from inp.txt.
#ifndef ONLINE_JUDGE
    FILE* temp = freopen("inp.txt", "r", stdin);
#endif

    int n, windowSize;
    if (!(cin >> n >> windowSize)) return 0;

    long long x, a, b, c;
    cin >> x >> a >> b >> c;

    // Pre-allocate array
    vector<long long> arr(n);
    for (int i = 0; i < n; ++i) {
        arr[i] = x;
        x = (a * x + b) % c;
    }

    // Maintain count of set bits in the current window
    vector<int> window(BITS, 0);

    // Process the first window
    for (int i = 0; i < windowSize && i < n; ++i) {
        for (int j = 0; j < BITS; ++j) {
            if (arr[i] & (1LL << j)) {
                window[j]++;
            }
        }
    }

    long long ans = getNumFromWindow(window);

    // Slide the window
    for (int i = windowSize; i < n; ++i) {
        for (int j = 0; j < BITS; ++j) {
            // Remove the outgoing element's bits
            if (arr[i - windowSize] & (1LL << j)) {
                window[j]--;
            }
            // Add the incoming element's bits
            if (arr[i] & (1LL << j)) {
                window[j]++;
            }
        }
        ans ^= getNumFromWindow(window);
    }

    cout << ans << "\n";

    return 0;
}