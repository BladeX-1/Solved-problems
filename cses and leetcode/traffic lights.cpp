#include <iostream>
#include <vector>
#include <set>

using namespace std;


int main(){
    // Fast I/O is required for CSES Traffic Lights
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int x,n;
    cin>>x>>n;

    multiset<int,greater<int>> clearRoadSegments;
    clearRoadSegments.insert(x-0);

    set<int> points;
    points.insert(0);
    points.insert(x);

    int trafficLightPoint;
    for(int i=0;i<n;i++){
        cin>>trafficLightPoint;

        auto p = points.upper_bound(trafficLightPoint);
        int r = *p;
        p--;
        int l=*p;

        auto q = clearRoadSegments.find(r-l);
        clearRoadSegments.erase(q);

        points.insert(trafficLightPoint);
        clearRoadSegments.insert(trafficLightPoint-l);
        clearRoadSegments.insert(r-trafficLightPoint);

        int s = *clearRoadSegments.begin();
        cout<<s<<' ';

    }

}