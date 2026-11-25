#include <iostream>
#include <vector>
#include <complex>
#include <cmath>
#include <fstream>
#include <chrono>

using namespace std;

const double PI = acos(-1.0);
using cd = complex<double>;

// Combined fft and ifft logic into a single recursive function
void fft(vector<cd>& p, bool invert) {
    int n = p.size();
    if (n == 1) return;

    vector<cd> evens(n / 2), odds(n / 2);
    for (int i = 0; 2 * i < n; i++) {
        evens[i] = p[2 * i];
        odds[i] = p[2 * i + 1];
    }

    fft(evens, invert);
    fft(odds, invert);

    // If invert is true, the angle is negative (for ifft)
    double angle = 2 * PI / n * (invert ? -1 : 1);
    cd w(1), wn(cos(angle), sin(angle));
    
    for (int i = 0; i < n / 2; i++) {
        p[i] = evens[i] + w * odds[i];
        p[i + n / 2] = evens[i] - w * odds[i];
        w *= wn;
    }
}

int main() {
    // Optimize standard I/O operations for speed
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Replicate the local system file detection
    ifstream flagfile("__localsystemflag__");
    if (flagfile.good()) {
        freopen("inp.txt", "r", stdin);
    }

    int k, apples, bananas;
    if (!(cin >> k >> apples >> bananas)) return 0;

    // Calculate fftsize as the next power of 2 >= 2*k
    int fftsize = 1;
    while (fftsize < 2 * k) {
        fftsize *= 2;
    }

    // Initialize arrays padded to fftsize with zeros
    vector<cd> applesArr(fftsize, 0);
    for (int i = 0; i < apples; i++) {
        int x;
        cin >> x;
        if (x <= k) applesArr[x] += 1.0;
    }

    vector<cd> bananaArr(fftsize, 0);
    for (int i = 0; i < bananas; i++) {
        int x;
        cin >> x;
        if (x <= k) bananaArr[x] += 1.0;
    }

    // Start timer
    // auto start = chrono::high_resolution_clock::now();

    // Perform FFT
    fft(applesArr, false);
    fft(bananaArr, false);

    // Point-wise multiplication
    vector<cd> pointWise(fftsize);
    for (int i = 0; i < fftsize; i++) {
        pointWise[i] = applesArr[i] * bananaArr[i];
    }

    // Perform Inverse FFT
    fft(pointWise, true);
    for (int i = 0; i < fftsize; i++) {
        pointWise[i] /= fftsize;
    }

    // Extract, absolute, round, and print the results from index 2 to 2*k
    for (int i = 2; i <= 2 * k; i++) {
        long long val = round(abs(pointWise[i]));
        cout << val << (i == 2 * k ? "" : " ");
    }
    cout << "\n";

    // Stop timer and print execution time
    // auto end = chrono::high_resolution_clock::now();
    // chrono::duration<double> diff = end - start;
    // cout << diff.count() << "\n";

    return 0;
}