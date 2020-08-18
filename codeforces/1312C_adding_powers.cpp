#include <iostream>
#include <cstring>
using namespace std;

#define ll long long

ll a[30], c[60];
int n, k;

void solve(){
    cin >> n >> k;
    memset(c, 0, sizeof(c));
    for(int i=0; i<n; i++){
        cin >> a[i];
        int j=0;
        while(a[i]){
            c[j] += a[i]%k;
            j++;
            a[i] /= k;
        }
    }
    for(int i=0; i<60; i++){
        if(c[i]>1){
            cout << "NO\n";
            return;
        }
    }
    cout << "YES\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;
    while(t--){
        solve();
    }
}
