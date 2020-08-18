#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;
    while(t--){
        int m, n;
        cin >> m >> n;
        cout << (m%n==0? "YES":"NO") << endl;
    }
}
