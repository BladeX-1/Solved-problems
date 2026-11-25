#include <iostream>
#include <vector>

using namespace std;

const long long M = 1e9 + 7;

// Define a type alias for a 2D matrix to keep the code clean
typedef vector<vector<long long>> matrix;

// Matrix multiplication
matrix matMult(const matrix& m1, const matrix& m2) {
    int n = m1.size();
    matrix m3(n, vector<long long>(n, 0));
    
    // The loop order (i, k, j) is used instead of (i, j, k) for better cache locality (faster execution)
    for (int i = 0; i < n; i++) {
        for (int k = 0; k < n; k++) {
            for (int j = 0; j < n; j++) {
                m3[i][j] += (m1[i][k] * m2[k][j]) % M;
                m3[i][j] %= M;
            }
        }
    }
    return m3;
}

// Matrix exponentiation using iterative method (Binary Exponentiation)
matrix matPower(matrix base, long long p) {
    int n = base.size();
    matrix res(n, vector<long long>(n, 0));
    
    // Initialize res as the identity matrix
    for (int i = 0; i < n; i++) {
        res[i][i] = 1;
    }
    
    while (p > 0) {
        // If p is odd, multiply res with base
        if (p % 2 == 1) {
            res = matMult(res, base);
        }
        // Square the base and halve the power
        base = matMult(base, base);
        p /= 2;
    }
    return res;
}

int main() {
    // Fast I/O for competitive programming
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    /* 
    Optional: To read from a local file like in your Python code, 
    you can uncomment the next two lines:
    */
    // #ifndef ONLINE_JUDGE
    // freopen("inp.txt", "r", stdin);
    // #endif

    long long n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    matrix mat(n, vector<long long>(n, 0));
    
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        mat[a - 1][b - 1]++;
    }

    matrix powerk = matPower(mat, k);
    
    cout << powerk[0][n - 1] << "\n";

    return 0;
}