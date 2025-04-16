import java.util.*;
class topologicalsort{
    public static void topo(int v, List<List<Integer>>adj){
        int [] vis =new int[v];
        Arrays.fill(vis,0);
        Stack<Integer>st=new Stack<>();
        for(int i=0;i<v;i++){
            if(vis[i]==0){
                dfs(i,adj,vis,st);
            }
        }
        System.out.println("Topological Order: ");
        while(!st.isEmpty()){
            System.out.println(st.pop()+" ");
        }
    }
    private static void dfs(int node, List<List<Integer>> adj, int[] vis, Stack<Integer>st){
        vis[node]=1;
        for(int neigh: adj.get(node)){
            if(vis[neigh]==0){
                dfs(neigh, adj, vis,st);
            }
        }
        st.push(node);
    }
    public static void main(String[] args){
        int v=6;
        List<List<Integer>>adj=new ArrayList<>();
        for(int i=0;i<v;i++){
            adj.add(new ArrayList<>());
        }
        adj.get(5).add(2);
    }
}