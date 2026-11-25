#include <iostream>
#include <vector>
#include <complex>
#include <cmath>
#include <algorithm>
#include <fstream>

using namespace std;

// Define a type alias for complex numbers for cleaner code
typedef complex<double> cd;
const double PI = acos(-1.0);

// Combines both fft and ifft. Set invert=true for ifft.
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

    // e^(2*pi*i/n) for FFT, and e^(-2*pi*i/n) for IFFT
    double ang = 2 * PI / n * (invert ? -1 : 1);
    cd w(1), wn(cos(ang), sin(ang));
    
    for (int i = 0; 2 * i < n; i++) {
        a[i] = a0[i] + w * a1[i];
        a[i + n / 2] = a0[i] - w * a1[i];
        
        // Dividing by 2 at each recursion depth level accomplishes 
        // the same thing as dividing by N at the very end.
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

    // Read inputs
    int lenSig, lenMask;
    if (!(cin >> lenSig >> lenMask)) return 0;

    vector<int> sig_in(lenSig);
    for (int i = 0; i < lenSig; i++) {
        cin >> sig_in[i];
    }

    vector<int> mask_in(lenMask);
    for (int i = 0; i < lenMask; i++) {
        cin >> mask_in[i];
    }

    // Calculate maxLen as the next power of 2
    int maxLen = lenSig + lenMask - 1;
    int n = 1;
    while (n < maxLen) n <<= 1;
    maxLen = n;

    // Reverse the mask
    reverse(mask_in.begin(), mask_in.end());

    // Initialize arrays padded with zeros
    vector<cd> sig(maxLen, 0.0);
    vector<cd> mask(maxLen, 0.0);

    for (int i = 0; i < lenSig; i++) sig[i] = sig_in[i];
    for (int i = 0; i < lenMask; i++) mask[i] = mask_in[i];

    // Perform FFT on both
    fft(sig, false);
    fft(mask, false);

    // Point-wise multiplication
    vector<cd> resultFFT(maxLen);
    for (int i = 0; i < maxLen; i++) {
        resultFFT[i] = sig[i] * mask[i];
    }

    // Perform Inverse FFT
    fft(resultFFT, true);

    // Format and print the result
    int outLen = lenSig + lenMask - 1;
    for (int i = 0; i < outLen; i++) {
        // Equivalent to round(abs(x))
        long long val = round(abs(resultFFT[i]));
        cout << val << (i == outLen - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}