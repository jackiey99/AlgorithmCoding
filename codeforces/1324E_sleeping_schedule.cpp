#include <iostream>
#include <climits>
#include <cstring>
#include <algorithm>
using namespace std;

#define ll long long
#define ar array

const int N = 2345;
int n, h, l, r;
int a[N];
int dp[N][N];

void solve() {
    cin >> n >> h >> l >> r;

    for (int i = 0; i < N; i++) {
        fill_n(dp[i], N, -1e9);
    }
    dp[0][0] = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        for (int j = 0; j < h; j++) {
            if (dp[i][j]>=0) {
                int nj = (j + a[i]) % h;
                dp[i + 1][nj] = max(dp[i + 1][nj], dp[i][j] + (l <= nj && nj <= r));
                nj = (j + a[i] - 1) % h;
                dp[i + 1][nj] = max(dp[i + 1][nj], dp[i][j] + (l <= nj && nj <= r));
            }
        }
    }
    cout << *max_element(dp[n], dp[n] + h) << "\n";
}

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0);
    solve();
    return 0;
}
