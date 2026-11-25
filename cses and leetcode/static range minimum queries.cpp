#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

// Global vectors to avoid passing them deeply into recursive calls
vector<int> arr;
vector<int> segmentTreeMinimum;

void fillTree(int arrl, int arrr, int i) {
    if (arrl == arrr) {
        segmentTreeMinimum[i] = arr[arrl];
        return;
    }
    int arrm = arrl + (arrr - arrl) / 2;
    fillTree(arrl, arrm, i * 2 + 1);       // towards left child
    fillTree(arrm + 1, arrr, i * 2 + 2);   // towards right child
    
    segmentTreeMinimum[i] = min(segmentTreeMinimum[2 * i + 1], segmentTreeMinimum[2 * i + 2]);
}

int getMin(int i, int arrl, int arrh, int segl, int segh) {
    if (arrl <= segl && segh <= arrh) {
        return segmentTreeMinimum[i];
    } else if (arrh < segl || segh < arrl) {
        return INT_MAX; // Represents float('inf')
    }
    
    int mid = segl + (segh - segl) / 2;
    int left = getMin(2 * i + 1, arrl, arrh, segl, mid);
    int right = getMin(2 * i + 2, arrl, arrh, mid + 1, segh);
    
    return min(left, right);
}

int main() {
    // Fast I/O (Equivalent to sys.stdin.readline)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // C++ equivalent for the local vs server file loading boilerplate
    // Uncomment these lines when running locally to read from inp.txt
    /*
    #ifndef ONLINE_JUDGE
        if (freopen("inp.txt", "r", stdin) == NULL) {
            // fallback to stdin if file is missing
        }
    #endif
    */

    int n, q;
    if (!(cin >> n >> q)) return 0;

    arr.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    // Initialize segment tree with infinity
    segmentTreeMinimum.assign(4 * n, INT_MAX);
    fillTree(0, n - 1, 0);

    vector<int> ansarr;
    ansarr.reserve(q); // Optimization to prevent reallocation
    for (int k = 0; k < q; ++k) {
        int a, b;
        cin >> a >> b;
        int ans = getMin(0, a - 1, b - 1, 0, n - 1);
        ansarr.push_back(ans);
    }

    // Print space-separated results
    for (size_t i = 0; i < ansarr.size(); ++i) {
        cout << ansarr[i] << (i == ansarr.size() - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}