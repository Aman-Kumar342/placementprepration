import java.util.*;
class dails{
    static class edge{
        int to, weight;
        edge(int to, int weight){
            this.to=to;
            this.weight=weight;
        }
    }
    public static void dialsalgo(int N, int src, List<List<edge>>adj, int w){
        int inf=Integer.MAX_VALUE;
        int[]dist=new int [N];
        Arrays.fill(dist,inf);
        dist[src]=0;

        // made of bukset to store the node
        List<Deque<Integer>> buckets = new ArrayList<>();
        for(int i=0;i<=w*N; i++){
            buckets.add(new LinkedList<>());
        }
        // enter the source node in bucket 
        buckets.get(0).add(src);

//process the bucket

        for(int d=0;d<=w*N;d++){
            while(!buckets.get(d).isEmpty()){
                int u=buckets.get(d).poll();
                if(dist[u]<d) continue;

                for(edge e : adj.get(u)){
                    int v=e.to,weight=e.weight;
                    if(dist[v]>dist[u]+weight){
                        dist[v]=dist[u]+weight;
                        buckets.get(dist[v].add(v));
                    }
                }

            }
        }

        
        // print shortest distance 
        for(int i=0;i<N;i++){
            System.out.println("distance");
        }


    }
    public static void main(String[] args){
        int N=5;
        List<List<edge>> adj=new ArrayList<>();
        for(int i=0;i<N;i++){
            adj.add(new ArrayList<>());
        }
        adj.get(0).add(new edge(1,2));
        adj.get(1).add(new edge(2,1));
        adj.get(1).add(new edge(3,3));
        adj.get(2).add(new edge(4,4));
        adj.get(3).add(new edge(4,2));

        int maxweight=4;
        dials(N,0,adj,maxweight);
    }
}