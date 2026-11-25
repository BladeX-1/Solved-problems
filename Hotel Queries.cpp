#include <iostream>
#include <set>
#include <map>
#include <fstream>

using namespace std;

ifstream inputfile("inp.txt");

int main(){
    map<int,set<int>> hotels;

    int n,m;
    inputfile>>n>>m;
    // cin>>n>>m;

    int x;
    // fill up the hotels map
    for(int i=0;i<n;i++){
        inputfile>>x;
        // cin>>x;
        if(hotels.find(x)==hotels.end()){
            hotels[x] = set<int>();
        }
        hotels[x].insert(i);
    }

    // cout<<"hello";
    // if(true){
    //     auto it = hotels.begin();
    //     while(it!=hotels.end()){
    //         cout<<it->first<<' ';
    //         it++;
    //     }
    //     cout<<endl;
    // }

    int group;
    for(int i=0;i<m;i++){
        // cin>>group;
        inputfile>>group;
        auto it = hotels.lower_bound(group);
        // cout<<"group"<<' '<<group<<endl;
        // cout<<"it "<<it->first<<' '<<(it==hotels.end())<<endl;
        if(it==hotels.end()){
            cout<<-1+1<<' ';

        }
        else{
            cout<<*(it->second).begin()+1<<' ';
            (it->second).erase(*(it->second).begin());
            if((it->second).empty()){
                hotels.erase(it->first);
            }
        }
    }


    return 0;
}