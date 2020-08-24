#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

#define ll long long

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--){
        int n;
        cin >> n;
        int a[n];
        bool even=0, odd=0;
        for(int i=0;i<n;i++){
            cin >> a[i];
            if(a[i]&1)
                odd=1;
            else
                even=1;
        }
        cout << (even&&odd?"NO":"YES") << endl;
    }
}
