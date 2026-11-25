#include <iostream>
#include <vector>
#include <cmath>
#include <unordered_map>
#include <map>

using namespace std;

const int M = 1000000007;

// Cache to store the DP states, equivalent to Python's aReach
// aReach[a][step][val] -> frequency
unordered_map<int, vector<unordered_map<int, long long>>> aReach;

int n, m;

long long single_ways(int a, int k) {
    if (k == 0) return 1;
    
    a = min(a, m - a + 1);
    int maxReach = a + k;
    int minReach = a - k;

    if (1 <= minReach && maxReach <= m) {
        a += -minReach + 1;
    }

    if (aReach.find(a) == aReach.end()) {
        unordered_map<int, long long> c;
        if (a - 1 >= 1) c[a - 1] = 1;
        if (a + 1 <= m) c[a + 1] = 1;
        c[a] += 1;
        aReach[a].push_back(c);
    }

    while (aReach[a].size() < k) {
        unordered_map<int, long long> lastC = aReach[a].back();
        unordered_map<int, long long> newC = lastC; // copy
        
        for (auto const& [ky, f] : lastC) {
            if (ky - 1 >= 1) {
                newC[ky - 1] = (newC[ky - 1] + f) % M;
            }
            if (ky + 1 <= m) {
                newC[ky + 1] = (newC[ky + 1] + f) % M;
            }
        }
        aReach[a].push_back(newC);
    }

    long long total = 0;
    for (auto const& [ky, f] : aReach[a][k - 1]) {
        total = (total + f) % M;
    }
    return total;
}

long long double_ways(int a, int b, int k) {
    if (k == 0) return 1;
    
    int min_ab = min(a, b);
    int max_ab = max(a, b);
    a = min_ab;
    b = max_ab;
    
    if (m - b + 1 < a) {
        a = m - max_ab + 1;
        b = m - min_ab + 1;
    }

    int minReach = a - k;
    int maxReach = a + k;

    if (!(minReach - 1 <= b && b <= maxReach + 1)) {
        return 0;
    }

    if (aReach.find(a) == aReach.end()) {
        unordered_map<int, long long> c;
        if (a - 1 >= 1) c[a - 1] = 1;
        if (a + 1 <= m) c[a + 1] = 1;
        c[a] += 1;
        aReach[a].push_back(c);
    }

    while (aReach[a].size() < k + 1) {
        unordered_map<int, long long> lastC = aReach[a].back();
        unordered_map<int, long long> newC = lastC; // copy
        
        for (auto const& [ky, f] : lastC) {
            if (ky - 1 >= 1) {
                newC[ky - 1] = (newC[ky - 1] + f) % M;
            }
            if (ky + 1 <= m) {
                newC[ky + 1] = (newC[ky + 1] + f) % M;
            }
        }
        aReach[a].push_back(newC);
    }

    return aReach[a][k][b]; // It defaults to 0 if 'b' is not present
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> n >> m)) return 0;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    for (int i = 0; i < n - 1; i++) {
        if (arr[i] != 0 && arr[i + 1] != 0 && abs(arr[i] - arr[i + 1]) > 1) {
            cout << 0 << "\n";
            return 0;
        }
    }

    vector<int> starts;
    vector<int> ends;

    for (int i = 0; i < n; i++) {
        if (arr[i] == 0 && (i == 0 || arr[i - 1] != 0)) {
            starts.push_back(i);
        }
        if (arr[i] == 0 && (i == n - 1 || arr[i + 1] != 0)) {
            ends.push_back(i);
        }
    }

    long long ans = 1;
    if (starts.empty()) {
        cout << 1 << "\n";
        return 0;
    }

    if (starts[0] == 0 && ends[0] == n - 1) { // everything is zero
        long long temp = 0;
        for (int i = 1; i <= m; i++) {
            temp = (temp + single_ways(i, n - 1)) % M;
        }
        ans = (ans * temp) % M;
        cout << ans << "\n";
        return 0;
    }

    if (starts[0] == 0) {
        ans = (ans * single_ways(arr[ends[0] + 1], ends[0] - starts[0] + 1)) % M;
        starts.erase(starts.begin());
        ends.erase(ends.begin());

        if (starts.empty()) {
            cout << ans << "\n";
            return 0;
        }
    }

    if (ends.back() == n - 1) {
        ans = (ans * single_ways(arr[starts.back() - 1], ends.back() - starts.back() + 1)) % M;
        starts.pop_back();
        ends.pop_back();

        if (starts.empty()) {
            cout << ans << "\n";
            return 0;
        }
    }

    for (size_t i = 0; i < starts.size(); i++) {
        ans = (ans * double_ways(arr[starts[i] - 1], arr[ends[i] + 1], ends[i] - starts[i] + 1)) % M;
    }

    cout << ans << "\n";
    return 0;
}