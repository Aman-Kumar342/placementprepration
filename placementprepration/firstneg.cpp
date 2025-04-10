#include<bits/stdc++.h>
using namespace std;
vector<int>firstneg(vector<int>arr,int k){
    int n=arr.size();
    queue<int>q;
    vector<int>ans;
    int i=0;
    int j=0;
    while(j<n){
        if(arr[j]<0){
            q.push(arr[j]);
        }
        if((j-i+1)<k){
            j++;
        }
        else if((j-i+1)==k){
            if(q.empty()){
                ans.push_back(0);
            }
            else {
                ans.push_back(q.front());
                if(arr[i]==q.front()){
                    q.pop();
                }

            }
        }
        i++;
        j++;
    }

}
int main(){
    int n;
    cin>>n;
    int k;
    cin>>k;
    vector<int>arr(n);
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    vector<int>res=firstneg(arr,k);
    for(int i=0;i<res.size();i++){
        cout<<res[i]<<" ";
    }
    return 0;

}