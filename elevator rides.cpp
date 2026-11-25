#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <set>
#include <cassert>

using namespace std;

int n;
long long capacity;
vector<long long> weights;
int allOnes;

// Using std::set for memoization of the (bitmask, capacityLeft) tuples
set<pair<int, long long>> memo;

void fillRound(int includedBitmask, int start, long long capacityLeft, unordered_set<int>& accum) {
    if (memo.count({includedBitmask, capacityLeft})) {
        return;
    }
    memo.insert({includedBitmask, capacityLeft});

    if (includedBitmask == allOnes) { // all done
        accum.insert(includedBitmask);
        return;
    }

    for (int i = n - 1; i >= 0; --i) {
        if (includedBitmask & (1 << i)) {
            continue;
        } else if (capacityLeft < weights[i]) { // capacity smaller than smallest weight
            accum.insert(includedBitmask);
            return;
        } else {
            break;
        }
    }

    if (start == n) { // can fill more, but reached end
        return;
    }

    for (int i = start; i < n; ++i) {
        if (includedBitmask & (1 << i)) continue;
        if (weights[i] > capacityLeft) continue;
        if (i != start && weights[start] == weights[i]) continue;

        fillRound(includedBitmask | (1 << i), i + 1, capacityLeft - weights[i], accum);
        if (accum.count(allOnes)) {
            return;
        }
    }
}

int f() {
    int round = 0;
    unordered_set<int> newAns;
    newAns.insert(0);

    while (!newAns.count(allOnes)) {
        unordered_set<int> ans = newAns;
        newAns.clear();
        round++;

        assert(!ans.empty());

        for (int a : ans) {
            int tempx = a;
            int start = 0;
            while (tempx & 1) {
                tempx >>= 1;
                start++;
            }
            
            unordered_set<int> temp;
            fillRound(a | (1 << start), start + 1, capacity - weights[start], temp);
            
            if (temp.count(allOnes)) {
                return round;
            }
            
            for (int val : temp) {
                newAns.insert(val);
            }
        }
        
        // C++ equivalent for debug printing if needed:
        // for (int val : newAns) cout << val << " "; cout << "\n";
    }
    assert(false);
    return -1;
}

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> n >> capacity)) return 0;
    
    weights.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> weights[i];
    }

    sort(weights.rbegin(), weights.rend());

    vector<long long> rightCumulative;
    rightCumulative.push_back(0);
    for (int i = n - 1; i >= 0; --i) {
        rightCumulative.push_back(rightCumulative.back() + weights[i]);
    }
    reverse(rightCumulative.begin(), rightCumulative.end());

    // try greedy filling
    long long bucket = 0;
    int count = 1;
    for (int i = 0; i < n; ++i) {
        if (bucket + weights[i] <= capacity) {
            bucket += weights[i];
        } else {
            count++;
            bucket = weights[i];
        }
    }
    int bestAns = count;

    allOnes = (1 << n) - 1;

    int ans = f();
    cout << ans << "\n";

    return 0;
}