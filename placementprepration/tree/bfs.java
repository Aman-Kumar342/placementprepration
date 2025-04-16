import java.util.*;
class TreeNode{
    int val;
    TreeNode left ,right;
    TreeNode(int val){
        this.val=val;
        this.left=null;
        this.right=null;
    }
}
public class bfs{
    public static List<Integer>Bfstraversal(List<List<Integer>> adj){
        int v=adj.size();
        List<Integer>bfst =new ArrayList<>();
        int[] vis = new int[v];
        vis[0]=1;
        Queue<Integer>q=new LinkedList<>();
        q.add(0);
        while(!q.isEmpty()){
            int node=q.poll();
            bfst.add(node);
            for(int it : adj.get(node)){
                if(vis[it]==0){
                    vis[it]=1;
                    q.add(it);
                }
            }
        }
        return bfst;
    }
}