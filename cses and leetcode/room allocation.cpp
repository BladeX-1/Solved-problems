#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
    // Equivalent to your local env check. 
    // Most CP servers define 'ONLINE_JUDGE', so this runs only on your local machine.
    #ifndef ONLINE_JUDGE
    if (freopen("inp.txt", "r", stdin) == nullptr) {
        // Fallback to standard input if file doesn't exist
    }
    #endif

    // Fast I/O (Equivalent to sys.stdin.readline)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    // Store customers as tuples: {arrival, departure, original_index}
    vector<tuple<int, int, int>> customers(n);
    for (int i = 0; i < n; ++i) {
        int a, b;
        cin >> a >> b;
        customers[i] = {a, b, i};
    }

    // Sort by arrival time
    sort(customers.begin(), customers.end());

    // Min-heap for active customers: {departure, original_index, room_number}
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> heap;
    
    // Min-heap for empty rooms
    priority_queue<int, vector<int>, greater<int>> emptyRooms;
    
    // Initial batch of 10 rooms
    for (int i = 0; i < 10; ++i) {
        emptyRooms.push(i);
    }
    int nextEmpty = 10;

    vector<int> allocation(n, -99);
    int ans = 0;

    for (int i = 0; i < n; ++i) {
        int a = get<0>(customers[i]);
        int b = get<1>(customers[i]);
        int idx = get<2>(customers[i]);

        // Free rooms whose departure time is strictly less than current arrival time
        while (!heap.empty() && get<0>(heap.top()) < a) {
            auto leavingCustomer = heap.top();
            heap.pop();
            emptyRooms.push(get<2>(leavingCustomer)); // push the freed room
        }

        // Get a new room
        int newRoom = emptyRooms.top();
        emptyRooms.pop();

        // Push the customer to the active heap
        heap.push({b, idx, newRoom});

        // Replenish emptyRooms by 10 if it runs out (matching your Python logic)
        if (emptyRooms.empty()) {
            for (int r = nextEmpty; r < nextEmpty + 10; ++r) {
                emptyRooms.push(r);
            }
            nextEmpty += 10;
        }

        allocation[idx] = newRoom;
        ans = max(ans, (int)heap.size());
    }

    // Output answer
    cout << ans << "\n";
    for (int i = 0; i < n; ++i) {
        // x + 1 mapping for 1-based indexing
        cout << allocation[i] + 1 << (i == n - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}