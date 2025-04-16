#include<bits/stdc++.h>
using namespace std;
int countan(string s, string p){
    int ans=0;
    int k=p.size();
    int n=s.size();
    map<char,int>mp;
    for(auto it : p){
        mp[it]++;
    }
    int count=mp.size();
    int i=0;
    int j=0;
    while(j<n){
        if(mp.find(s[j])!=mp.end()){
            mp[s[j]]--;
            if(mp[s[j]]==0){
                count--;
            }
        }
        if((j-i+1)<k){
            j++;
        }
        else if((j-i+1)==k){
            if(count==0){
                ans++;
            }
            if(mp.find(s[i])!=mp.end()){
                mp[s[i]]++;
            }
            if(mp[s[i]]==1){
                count++;
            }
        }
        i++;
        j++;
    }
}
int main(){
    return 0;

}