#include <iostream>
#include <vector>
using namespace std;

#define ll long long
#define ar array

const int N=2e5;
int n, a[N], ans[N], dp[N];
vector<int> adj[N];

void dfs(int u, int p=-1){
    dp[u] = a[u];
    for(int v: adj[u]){
        if(v==p)
            continue;
        dfs(v, u);
        dp[u] += max(dp[v], 0);
    }
}

void dfs2(int u, int p=-1){
    ans[u] = dp[u];
    for(int v: adj[u]){
        if(v==p)
            continue;
        dp[u] -= max(0, dp[v]);
        dp[v] += max(0, dp[u]);
        dfs2(v, u);
        dp[v] -= max(0, dp[u]);
        dp[u] += max(0, dp[v]);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for(int i=0;i<n;i++){
        cin >> a[i];
        if(a[i]==0){
            a[i] = -1;
        }
    }
    for(int i=1, u, v; i<n;i++){
        cin >> u >>v;
        u--;
        v--;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    dfs(0);
    dfs2(0);
    for(int i=0;i<n;i++){
        cout << ans[i] << " ";
    }
}
