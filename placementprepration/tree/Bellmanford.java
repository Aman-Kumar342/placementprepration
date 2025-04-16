import java.util.*;
class Edge{
    int src, dest, weight;
    Edge(int src, int dest, int weight){
        this.src=src;
        this.dest=dest;
        this.weight=weight;
    }
}
public class Bellmanford{
    public static void bellmanford(List<Edge>edge, int v, int source){
        int [] dist=new int[v];
        Arrays.fill(dist,Integer.MAX_VALUE);
        dist[source]=0;
        for(int i=0;i<v-1;i++){
            for(Edge eg: edge){
                if(dist[eg.src]!=Integer.MAX_VALUE && dist[eg.src]+eg.weight<dist[eg.dest]){
                    dist[eg.dest]=dist[eg.src]+eg.weight;
                }
            }
        }
    }
}