#include <iostream>
#include <vector>
#include <complex>
#include <cmath>
#include <algorithm>
#include <fstream>
#include <string>

using namespace std;

typedef complex<double> cd;
const double PI = acos(-1.0);

// Unified FFT/IFFT function
void fft(vector<cd>& a, bool invert) {
    int n = a.size();
    if (n == 1) return;

    vector<cd> a0(n / 2), a1(n / 2);
    for (int i = 0; 2 * i < n; i++) {
        a0[i] = a[2 * i];
        a1[i] = a[2 * i + 1];
    }

    fft(a0, invert);
    fft(a1, invert);

    double ang = 2 * PI / n * (invert ? -1 : 1);
    cd w(1), wn(cos(ang), sin(ang));
    
    for (int i = 0; 2 * i < n; i++) {
        a[i] = a0[i] + w * a1[i];
        a[i + n / 2] = a0[i] - w * a1[i];
        
        if (invert) {
            a[i] /= 2;
            a[i + n / 2] /= 2;
        }
        w *= wn;
    }
}

int main() {
    // Replicate the local system flag check logic for I/O
    ifstream flagFile("__localsystemflag__");
    if (flagFile.good()) {
        flagFile.close();
        freopen("inp.txt", "r", stdin);
    }

    // Read the input as a single continuous string of digits
    string input_str;
    if (!(cin >> input_str)) return 0;

    int originalLength = input_str.length();
    if (originalLength == 0) return 0;

    // Calculate maxLen as the next power of 2 for (2 * originalLength - 1)
    int maxLen = 1;
    while (maxLen < 2 * originalLength - 1) {
        maxLen <<= 1;
    }

    // Initialize arrays padded with zeros
    vector<cd> s(maxLen, 0.0);
    vector<cd> srev(maxLen, 0.0);

    for (int i = 0; i < originalLength; i++) {
        s[i] = input_str[i] - '0';
        srev[i] = input_str[originalLength - 1 - i] - '0';
    }

    // Perform FFT on both
    fft(s, false);
    fft(srev, false);

    // Point-wise multiplication
    vector<cd> result(maxLen);
    for (int i = 0; i < maxLen; i++) {
        result[i] = s[i] * srev[i];
    }

    // Perform Inverse FFT
    fft(result, true);

    // Format and print the specific slice: result[originalLength : 2*originalLength-1]
    int endIdx = 2 * originalLength - 1;
    for (int i = originalLength; i < endIdx; i++) {
        long long val = round(abs(result[i]));
        cout << val << (i == endIdx - 1 ? "" : " ");
    }
    
    // Print a newline if the slice had elements
    if (originalLength < endIdx) cout << "\n";

    return 0;
}