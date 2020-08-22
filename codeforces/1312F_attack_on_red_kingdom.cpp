#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

#define ll long long
const int maxN=3e5;

int n, x, y, z, dp1[maxN], dp2[maxN], dp3[maxN], p;
ll a[maxN];

int mex(vector<int> a){
    sort(a.begin(), a.end());
    a.resize(unique(a.begin(), a.end()) - a.begin());
    a.push_back(maxN);
    for(int i=0; ;i++){
        if(i^a[i])
            return i;
    }
}

int get(int dp[maxN], ll a){
    if(a>200){
        return dp[(a-200)%p + 200];
    }
    return dp[a];
}
void solve(){
    cin >> n >> x >> y >> z;

    p = -1;
    for(int i=1; i<=300 && p<0; ++i){
        dp1[i] = mex({dp1[max(i-x, 0)], dp2[max(i-y, 0)], dp3[max(i-z, 0)]});
        dp2[i] = mex({dp1[max(i-x, 0)], dp3[max(i-z, 0)]});
        dp3[i] = mex({dp1[max(i-x, 0)], dp2[max(i-y, 0)]});

        bool ok = i>200;
        for(int k=0; k<5; ++k){
            ok &= dp1[200-k]==dp1[i-k] && dp2[200-k]==dp2[i-k] && dp3[200-k]==dp3[i-k];
        }
        if(ok){
            p=i;
        }
    }
    p -= 200;

    int sg = 0;
    for(int i=0; i<n; i++){
        cin >> a[i];
        sg ^= get(dp1, a[i]);
    }
    int ans = 0;
    for(int i=0; i<n; i++){
        sg ^= get(dp1, a[i]);
        if (!(sg^get(dp1, max(a[i]-x, 0ll)))){
            ans++;
        }
        if (!(sg^get(dp2, max(a[i]-y, 0ll)))){
            ans++;
        }
        if (!(sg^get(dp3, max(a[i]-z, 0ll)))){
            ans++;
        }
        sg ^= get(dp1, a[i]);
    }
    cout << ans << endl;
}
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--){
        solve();
    }
}
