#include <iostream>
#include <vector>

using namespace std;
string s;
int n;

void solve() {
    int t; cin >> t;
    while (t--) {
        cin >> s;
        n = s.size();
        vector<int> v;
        v.push_back(0);
        for (int i = 0; i < n; i++) {
            if (s[i] == 'R') {
                v.push_back(i + 1);
            }
        }
        v.push_back(n + 1);
        int res = 0;
        for (int i = 0; i + 1 < (int) v.size(); i++) {
            res = max(res, v[i + 1] - v[i]);
        }
        cout << res << "\n";
    }
}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}

