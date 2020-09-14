class Solution {
public:
    bool isTransformable(string s, string t) {
        int n = s.size();
        vector<deque<int>> pos(10);

        for(int i=0;i<n;i++)
            pos[s[i]-'0'].push_back(i);

        for(int i=0;i<n;i++){
            int num = t[i] - '0';
            if(pos[num].empty()) return false;

            int idx = pos[num].front();
            for(int j=0;j<num; j++){
                if(!pos[j].empty() && pos[j].front() < idx)
                    return false;
            }
            pos[num].pop_front();
        }
        return true;
    }
};
