#include <iostream>
#include <set>

using namespace std;


int main(){
    int n;
    int skip;
    cin>>n>>skip;

    set<int> people;
    for(int i=0;i<n;i++){
        people.insert(i);
    }

    int i = people.size()-1;
    while(people.size()>1){
        i+=skip%people.size();
        i%=people.size();
        
    }

    return 0;
}