#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define ll long long
#define ar array


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<int> cnt(n+1);
        for(int i=0;i<n;i++){
            int x;
            cin >> x;
            cnt[x]++;
        }
        int mx = *max_element(cnt.begin(), cnt.end());
        int diff = n + 1 - count(cnt.begin(), cnt.end(), 0);
        cout << max(min(mx-1, diff), min(mx, diff-1)) << endl;
    }

    return 0;
}
