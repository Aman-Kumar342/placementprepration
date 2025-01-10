import java.util.*;
public class ratinmaze{
    static void solve(int x, int y,int n,List<String>res,StringBuilder path,int [][] arr,List<Choice>choices){
        if(issolved(x,y,n)){
            res.add(path.toString());
            return;
        }
        for(Choice choice:choices){
            int newx=x+choice.dx;
            int newy=x+choice.dy;
            if(isvalid(newx , newy, n , arr)){
                arr[x][y]=0;
                path.append(choice.dname);
                solve(newx,newy,n,res,path,arr,choices);
                arr[x][y]=1;
                path.deleteCharAt(path.length()-1);
            } 
        }
    }
    public static boolean issolved(int x,int y,int n){
        return x==n-1 && y==n-1;
    }
    public static boolean isvalid(int x,int y,int n,int[][] arr){
        return x>=0 && x<n && y>=0 && y<n && arr[x][y]==1;
    }
    static class Choice{
        int dx;
        int dy;
        char dname;
        Choice(int dx,int dy,char dname){
            this.dx=dx;
            this.dy=dy;
            this.dname=dname;
        }
    }
    public static List<String>findpath(int[][] arr,int n){
        List<String>res=new ArrayList<>();
        StringBuilder path=new StringBuilder();
        List<Choice> choices=Arrays.asList(
            new Choice(-1,0,'u'),
            new Choice(1,0,'d'),
            new Choice(0,-1,'l'),
            new Choice(0,1,'r')
        );
        if(arr[0][0]==1){
            solve(0,0,n,res,path,arr,choices);
        }
        return res;
    }
    public static void mains(String [] args){
        int [][] maze={
            {1,0,0,0},
            {1,1,0,1},
            {0,1,0,0},
            {1,1,1,1}
        };
        int n=maze.length;
        List<String>paths=findpath(maze,n);
        if(paths.isEmpty()){
            System.out.println("No path found");
        }
        else{
            for(String path:paths){
                System.out.println(path);
            }
        }
    }
}
