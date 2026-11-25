#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>

using namespace std;

// Trie Node class
struct Node {
    int val;
    Node* zero;
    Node* one;
    
    Node() : val(-1), zero(nullptr), one(nullptr) {}
};

int digits;

// Recursive function to find the maximum XOR
int getBest(Node* a, Node* b, int i) {
    if (i == digits) {
        return a->val ^ b->val;
    }
    
    int ans = 0;
    if (a->one && b->zero) {
        int temp = getBest(a->one, b->zero, i + 1);
        ans = max(ans, temp);
    }
    if (a->zero && b->one) {
        int temp = getBest(a->zero, b->one, i + 1);
        ans = max(ans, temp);
    }

    if (!(a->one && b->zero) && !(a->zero && b->one)) {
        if (a->one && b->one) {
            int temp = getBest(a->one, b->one, i + 1);
            ans = max(ans, temp);
        } else if (a->zero && b->zero) {
            int temp = getBest(a->zero, b->zero, i + 1);
            ans = max(ans, temp);
        } else {
            assert(false);
        }
    }

    return ans;
}

/*
// Commented out in original Python code:
int query(Node* root, const string& num, int i) {
    if (i == digits) {
        return root->val; // Assuming root->val is already stored as int
    }
    
    if (num[i] == '0' && root->one) {
        return query(root->one, num, i + 1);
    } else if (num[i] == '1' && root->zero) {
        return query(root->zero, num, i + 1);
    } else if (root->one) {
        return query(root->one, num, i + 1);
    } else {
        return query(root->zero, num, i + 1);
    }
}
*/

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Uncomment the line below to read from "inp.txt" locally:
    // freopen("inp.txt", "r", stdin);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Prefix XOR array
    vector<int> cumu;
    cumu.push_back(0);
    for (int x : arr) {
        int last = cumu.back();
        cumu.push_back(last ^ x);
    }

    Node* preRoot = new Node();
    
    // Find max value to determine the number of bits
    int max_ = *max_element(cumu.begin(), cumu.end());
    if (max_ > 0) {
        digits = floor(log2(max_)) + 1;
    } else {
        digits = 1;
    }

    // Insert cumulative XORs into the Trie
    for (int x : cumu) {
        Node* r = preRoot;
        for (int i = 0; i < digits; i++) {
            if (((x >> (digits-1-i)) & 1) == 0) {
                if (!r->zero) {
                    r->zero = new Node();
                }
                r = r->zero;
            }
            if (((x >> (digits-1-i)) & 1) == 1) {
                if (!r->one) {
                    r->one = new Node();
                }
                r = r->one;
            }
        }
        r->val = x;
    }

    int ans = 0;
    if (preRoot->one && preRoot->zero) {
        ans = getBest(preRoot->one, preRoot->zero, 1);
    } else {
        ans = getBest(preRoot, preRoot, 0);
    }

    cout << ans << "\n";

    return 0;
}