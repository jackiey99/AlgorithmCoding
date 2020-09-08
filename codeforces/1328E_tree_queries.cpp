#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define ll long long
#define ar array

const int N=2e5;
int n, m, d[N], anc[N][18];
vector<int> adj[N];

void build_table(int u=0, int p=-1){
    anc[u][0]=p;
    for(int i=1;i<18;i++)
        anc[u][i] = anc[u][i-1]!= -1 ? anc[anc[u][i-1]][i-1]:-1;
    for(int v: adj[u]){
        if(v^p){
            d[v] = d[u]+1;
            build_table(v, u);
        }
    }
}

int lca(int u, int v){
    if(d[u]< d[v])
        swap(u, v);
    for(int i=17; i>=0; i--)
        if(d[u] - (1<<i) >= d[v])
            u = anc[u][i];
    if(u==v)
        return u;
    for(int i=17;i>=0;i--)
        if(anc[u][i]^anc[v][i])
            u=anc[u][i], v=anc[v][i];
    return anc[u][0];
}
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;
    for(int i=1, u, v; i< n; i++){
        cin >> u >> v;
        u--, v--;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    build_table();

    while(m--){
        int k;
        cin >> k;
        vector<int> query(k);
        for(int i=0;i<k;i++)
            cin >> query[i], query[i]--;
        // sort query vertices by depth
        sort(query.begin(), query.end(), [](const int &i, const int &j){
            return d[i] < d[j];
        });
        bool ok=1;
        for(int i=0;i<k-1&&ok; ++i){
            int w=lca(query[i], query[k-1]);
            ok = d[query[i]] <= d[w] + 1;
        }
        cout << (ok?"YES":"NO") << endl;

    }
    return 0;
}
