#include <iostream>
#include <vector>

using namespace std;

// Use long long for the segment tree to prevent integer overflow
// (Summing many large numbers will exceed 32-bit int capacity)
vector<long long> arr;
vector<long long> segmentTree;

void build(int i, int arrL, int arrR) {
    if (arrL == arrR) {
        segmentTree[i] = arr[arrL];
        return;
    }
    int arrM = arrL + (arrR - arrL) / 2;
    build(i * 2 + 1, arrL, arrM);
    build(i * 2 + 2, arrM + 1, arrR);
    segmentTree[i] = segmentTree[i * 2 + 1] + segmentTree[i * 2 + 2];
}

long long query(int i, int segL, int segR, int arrL, int arrR) {
    if (arrL <= segL && segR <= arrR) {
        return segmentTree[i];
    } else if (arrR < segL || segR < arrL) {
        return 0;
    }

    int segM = segL + (segR - segL) / 2;
    long long left = query(i * 2 + 1, segL, segM, arrL, arrR);
    long long right = query(i * 2 + 2, segM + 1, segR, arrL, arrR);

    return left + right;
}

long long update(int i, long long newValue, int k, int l, int r) {
    if (l == r && l == k) {
        long long delta = newValue - segmentTree[i];
        segmentTree[i] = newValue;
        return delta;
    }

    int m = l + (r - l) / 2;
    long long delta = 0;
    
    if (k <= m) {
        delta = update(2 * i + 1, newValue, k, l, m);
    } else {
        delta = update(2 * i + 2, newValue, k, m + 1, r);
    }

    segmentTree[i] += delta;
    return delta;
}

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    arr.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    // A recursive segment tree strictly requires 4*n space
    segmentTree.assign(4 * n, 0);
    build(0, 0, n - 1);

    vector<long long> ansarr;
    ansarr.reserve(q);

    for (int k_idx = 0; k_idx < q; ++k_idx) {
        int code;
        cin >> code;

        if (code == 1) {
            int a;
            long long b;
            cin >> a >> b;
            update(0, b, a - 1, 0, n - 1);
        } else {
            int a, b;
            cin >> a >> b;
            long long ans = query(0, 0, n - 1, a - 1, b - 1);
            ansarr.push_back(ans);
        }
    }

    // Print space-separated results
    for (size_t i = 0; i < ansarr.size(); ++i) {
        cout << ansarr[i] << (i == ansarr.size() - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}