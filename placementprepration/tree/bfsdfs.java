import java.awt.image.RescaleOp;
import java.util.*;
public class bfsdfs{
    public static List<Integer>bfstr(List<List<Integer>>adj){
        int v=adj.size();
        List<Integer>bfst=new ArrayList<>();
        int [] vis=new int [v];
        Queue<Integer>q=new LinkedList<>();
        vis[0]=1;
        q.add(0);
        while(!q.isEmpty()){
            int node=q.poll();
            bfst.add(node);
            for(int k : adj.get(node)){
                if(vis[k]==0){
                    vis[k]=1;
                    q.add(k);
                }
            }
        }
        return bfst;

    }
    private void dfshelper(int node , List<Integer>res, int[] vis, List<List<Integer>>adj){
        vis[node]=1;
        res.add(node);
        for(int it : adj.get(node)){
            if(vis[it]==0){
                vis[it]=1;
                dfshelper(it, res, vis,adj);

            }
        }
    }
    public static List<Integer>dfst(List<List<Integer>>adj){
        int v=adj.size();
        int []vis=new int [v];
        List<Integer>res;
        dfshelper(0,res,vis,adj);
        return res;
    }
    public static void main(String [] args){
        int v=6;
        List<List<Integer>>adj=new ArrayList<>();
        for(int i=0;i<v;i++){
            adj.add(new ArrayList<>());
        }
        adj.get(0).add(1);
        adj.get(1).add(2);
        adj.get(2).add(3);

    }
}