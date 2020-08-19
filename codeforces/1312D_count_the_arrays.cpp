#include <iostream>
#include <cstring>
using namespace std;

#define ll long long

const int M=998244353, maxN=2e5;
int n, m;
ll inv[maxN+1];

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    // calculate Modular Multiplicative Inverse:
    // https://cp-algorithms.com/algebra/module-inverse.html#:~:text=Practice%20Problems-,Definition,inverse%20does%20not%20always%20exist.
    inv[1]=1;
    for(int i=2; i<maxN; i++){
        inv[i] = M - M/i*inv[M%i]%M;
    }

    cin >> n >> m;
    ll ans=1;
    for(int i=0; i<n-3; i++){
        ans = ans*2%M;
    }
    for(int i=1; i<=m; i++){
        ans = ans*i%M;
    }
    for(int i=1; i<=n-1; i++){
        ans = ans*inv[i]%M;
    }
    for(int i=1; i<= m-n+1; i++){
        ans = ans*inv[i]%M;
    }
    ans = ans*(n-2)%M;
    cout << ans;
}
