class Solution {
    int memo[1001];
public:
    int maxJumps(vector<int>& arr, int d) {
        int n = arr.size();
        int ans = 0;
        for(int i=0;i<n;i++){
            dfs(i, arr, d);
            ans = max(ans, memo[i]);
        }
        return ans;
    }
    
    int dfs(int i, vector<int>& arr, int d){
        if(memo[i] != 0) return memo[i];
        int ans = 1;
        for(int k=1;k<=d;k++){
            if (i+k>=arr.size()) break;
            if(arr[i+k]>=arr[i]) break;
            ans = max(ans, dfs(i+k, arr, d) + 1);
        }
        
        for(int k=1;k<=d;k++){
            if (i-k <0) break;
            if(arr[i-k]>=arr[i]) break;
            ans = max(ans, dfs(i-k, arr, d) + 1);
        }
        memo[i] = ans;
        return ans;
    }
};
