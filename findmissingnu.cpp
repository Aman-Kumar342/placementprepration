#include<bits/stdc++.h>
using namespace std;
int main(){
    int m;
    cin>>m;
    int arr[m];
    for(int i=0;i<m;i++){
        cin>>arr[i];
    }
    int res=m*(m+1)/2;
    for(int i=0;i<m;i++){
        res=res-arr[i];
    }
    cout<<res;
    return 0;
}