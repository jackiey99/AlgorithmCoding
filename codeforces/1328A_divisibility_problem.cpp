#include <iostream>
#include <vector>
using namespace std;

#define ll long long
#define ar array

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t, a, b;
    cin >> t;
    while(t--){
        cin >> a >> b;
        if (a%b ==0)
            cout << 0 << endl;
        else
            cout << b - a%b << endl;
    }
}
