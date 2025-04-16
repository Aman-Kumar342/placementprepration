import java.util.*;
class dijkastra{
    static class Edge{
        int to, weight;
        Edge(int to, int weight){
            this.to=to;
            this.weight=weight;
        }
    }
    public static void dijkastraalgo(int n , int src, List<List<Edge>> adj){
        int INF=Integer.MAX_VALUE;
        int [] dist= new int[n];
        Arrays.fill(dist, INF);
        dist[src]=0;

        PriorityQueue<int[]>pq=new PriorityQueue<>(Comparator.comparing(a->a[0]));
        pq.add(new int[]{0,src}); // {dist,src}

        while(!pq.isEmpty()){
            int[] curr=pq.poll();
            int d=curr[0];  // current distance
            int u=curr[1];  //currnet node 

            if(d>dist[u])
                continue;
            
            for( Edge e: adj.get(u)){
                int v=e.to;
                int weight=e.weight;

                if(dist[v]>dist[u]+weight){
                    dist[v]=dist[u]+weight;
                    pq.add(new int[]{dist[v],v});
                }
            }
        }
        for(int i=0;i<n;i++){
            System.out.println("Distace from node "+ src + " to node "+ i + " is" + (dist[i]==INF ? "INF": dist[i]));

        }

    }


    public static void main(String[] args) {
        int N=5;
        List<List<Edge>>adj=new ArrayList<>();
        for(int i=0;i<N;i++){
            adj.add(new ArrayList<>());
        }

        adj.get(0).add(new Edge(1,2));

        dijkastraalgo(N, 0, adj);
    }

}
