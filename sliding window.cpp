#include <iostream>
#include <vector>

using namespace std;

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long n, windowSize;
    if (!(cin >> n >> windowSize)) return 0;

    long long x, a, b, c;
    cin >> x >> a >> b >> c;

    vector<long long> arr(n);
    for (long long i = 0; i < n; i++) {
        arr[i] = x;
        // Using __int128 to prevent any potential integer overflow 
        // if a, x, or b are very large (near 10^18)
        x = (long long)(((__int128)a * x + b) % c);
    }

    long long partitionSize = windowSize;
    
    // Compute prefix ORs within partitioned blocks
    vector<long long> orPre(n);
    for (long long i = 0; i < n; i++) {
        if (i % partitionSize == 0) {
            orPre[i] = arr[i];
        } else {
            orPre[i] = orPre[i - 1] | arr[i];
        }
    }

    // Compute suffix ORs within partitioned blocks
    vector<long long> orSuf(n);
    for (long long i = n - 1; i >= 0; i--) {
        if (i % partitionSize == partitionSize - 1 || i == n - 1) {
            orSuf[i] = arr[i];
        } else {
            orSuf[i] = orSuf[i + 1] | arr[i];
        }
    }

    long long xors = 0;
    
    // Evaluate sliding windows and immediately calculate XOR sum
    for (long long i = 0; i <= n - windowSize; i++) {
        long long suf = orSuf[i];
        long long pre = orPre[i + windowSize - 1];
        xors ^= (suf | pre);
    }

    cout << xors << "\n";

    return 0;
}