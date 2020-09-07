#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define ll long long
#define ar array

void solve(){
    int n;
    cin >> n;
    vector<int> a(n);
    for(int i=0;i<n;i++)
        cin >> a[i];
    bool same=true;
    for(int i=0; i<n; i++){
        if(a[i] != a[0])
            same=false;
    }
    if(same){ // only need one color
        cout << 1 << endl;
        for(int i=0;i<n;i++)
            cout << 1 << ' ';
        cout << endl;
        return;
    }

    if (n % 2 ==0){
        cout << 2 << endl;
        for(int i=0;i<n;i++){
            cout << 1 + (i&1) << ' ';
        }
        cout << endl;
        return;
    }

    for(int i=0;i<n;i++){
        if(a[i] == a[(i+1)%n]){
            cout << 2 << endl;
            for(int j=0;j<n;j++){
                cout << 1 + (1 & ( ( j-i-1+n)%n)) << ' ';
            }
            cout << endl;
            return;
        }
    }

    cout << 3 << endl;
    for(int i=0; i<n-1;i++)
        cout << 1 + (i&1) << ' ';
    cout << 3 << endl;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while(t--){
        solve();
    }

    return 0;
}
