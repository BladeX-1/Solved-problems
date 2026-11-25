#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

const long long INF = 1e18; // Equivalent to float('inf')

int n, q;
vector<long long> arr;
vector<long long> segment;

void build(int i, int arrL, int arrR) {
    if (arrL == arrR) {
        segment[i] = arr[arrL];
        return;
    }
    int arrM = arrL + (arrR - arrL) / 2;
    build(i * 2 + 1, arrL, arrM);
    build(i * 2 + 2, arrM + 1, arrR);
    segment[i] = min(segment[i * 2 + 1], segment[i * 2 + 2]);
}

long long query(int i, int segL, int segR, int arrL, int arrR) {
    if (arrL <= segL && segR <= arrR) {
        return segment[i];
    } else if (arrR < segL || segR < arrL) {
        return INF;
    }

    int segM = segL + (segR - segL) / 2;
    long long left = query(i * 2 + 1, segL, segM, arrL, arrR);
    long long right = query(i * 2 + 2, segM + 1, segR, arrL, arrR);

    return min(left, right);
}

void update(int i, long long newValue, int k, int l, int r) {
    if (l == r && l == k) {
        segment[i] = newValue;
        return;
    } 

    int m = l + (r - l) / 2;
    if (k <= m) {
        update(2 * i + 1, newValue, k, l, m);
    } else {
        update(2 * i + 2, newValue, k, m + 1, r);
    }

    segment[i] = min(segment[2 * i + 1], segment[2 * i + 2]);
}

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Equivalent to your local system flag check
    ifstream flagFile("__localsystemflag__");
    if (flagFile.good()) {
        flagFile.close();
        if (!freopen("inp.txt", "r", stdin)) {
            cerr << "Failed to open inp.txt" << endl;
        }
    }

    if (!(cin >> n >> q)) return 0;

    arr.resize(n);
    segment.assign(4 * n, -1);

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    if (n > 0) {
        build(0, 0, n - 1);
    }

    vector<long long> ansarr;
    
    for (int i = 0; i < q; i++) {
        int code;
        long long a, b;
        cin >> code >> a >> b;

        if (code == 1) {
            // Update operation: convert 1-based index 'a' to 0-based 'a-1'
            update(0, b, a - 1, 0, n - 1);
        } else {
            // Query operation: convert 1-based indices to 0-based
            long long ans = query(0, 0, n - 1, a - 1, b - 1);
            ansarr.push_back(ans);
        }
    }

    for (size_t i = 0; i < ansarr.size(); i++) {
        cout << ansarr[i] << (i == ansarr.size() - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}