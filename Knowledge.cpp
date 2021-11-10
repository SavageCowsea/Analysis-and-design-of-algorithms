#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, k;
    cin >> N;
    vector<int> v(N);
    vector<int> v1(N-1);
    for (int i = 0; i < N; i++) {
        cin >> k;
        v[i] = k;
    }
    for (int i = 0; i < N-1; i++) {
        cin >> k;
        v1[i] = k;
    }
    sort(v.begin(), v.end());
    
    sort(v1.begin(), v1.end());

    int ans = 0;
    for (int i = 0; i < N; i++) {
        if (i == N-1) ans = v[i];
        else if (v[i] != v1[i]) {
            ans = v[i];
            break;
        }
    }
    cout << ans <<'\n';
    
    
    
    return 0;
}
