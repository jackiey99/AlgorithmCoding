#include <iostream>
#include <string>
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
        string x;
        cin >> x;
        string a(n, '0'), b(n, '0');
        for(int i=0;i<n;i++){
            if (x[i]=='1'){
                a[i]='1';
                b[i]='0';
                for(int j=i+1;j<n;j++){
                    b[j]=x[j];
                }
                break;
            }else if(x[i]=='0'){
                a[i]=b[i]='0';
            }else{
                a[i]=b[i]='1';
            }

        }
        cout << a << endl << b << endl;
    }

}
