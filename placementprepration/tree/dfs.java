import java.util.*;
import java.io.*;
class TreeNode{
    int val;
    TreeNode left, right;
    TreeNode(int val){
        this.val=val;
        this.left=null;
        this.right=null;
    }
}
public class dfs{
    public void dfst(int node, List<Integer> res, List<List<Integer>> adj, int []vis){
        vis[node]=1;
        res.add(node);
        for(int i : adj.get(node)){
            if(vis[i]==0){
                vis[i]=1;
                res.add(i);
                dfst(i,res,adj,vis);
            }
        }
    }
    public static List<Integer>dfstraversal(List<List<Integer>>adj){
        int v=adj.size();
        List<Integer>ans;
        int [] vis=new int [v];
        dfst(0,ans,adj,vis);
        return ans; 

    }
}