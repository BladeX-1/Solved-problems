#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_set>

using namespace std;

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Replicate Python's local vs server file handling
    ifstream flag_file("__localsystemflag__");
    bool is_local = flag_file.good();
    flag_file.close();

    istream* input_stream = &cin;
    ifstream file_in;
    if (is_local) {
        file_in.open("inp.txt");
        if (file_in.is_open()) {
            input_stream = &file_in;
        }
    }

    // Read n and target
    long long n, target;
    if (!(*input_stream >> n >> target)) {
        return 0; // Safety check if input is empty
    }

    // Read array
    vector<long long> arr(n);
    for (int i = 0; i < n; ++i) {
        (*input_stream) >> arr[i];
    }

    // Process logic
    long long var = 0;
    long long count = 0;
    unordered_set<long long> cumuset;
    cumuset.insert(0);

    for (long long x : arr) {
        var += x;
        
        // Check condition matching Python's: var - target >= 0 and var - target in cumuset
        if (var - target >= 0 && cumuset.count(var - target)) {
            count++;
        }
        
        cumuset.insert(var);
    }

    cout << count << "\n";

    if (is_local && file_in.is_open()) {
        file_in.close();
    }

    return 0;
}