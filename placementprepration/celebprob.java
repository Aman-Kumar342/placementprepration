import java.util.*;
public class celebprob{
    public static boolean knows(int [][] matrix, int a, int b){
        return matrix[a][b]==1;
    }
    public static int findceleb(int [][] matrix,int n){
        Stack<Integer>st=new Stack<>();
        for(int i=0;i<n;i++){
            st.push(i);
        }
        while(st.size()>1){
            int a=st.pop();
            int b=st.pop();
            if(knows(matrix,a,b)){
                st.push(b);
            }
            else{
                st.push(a);
            }
        }
        int cand=st.pop();
        for(int i=0;i<n;i++){
            if(i!=cand){
                if(knows(matrix,cand,i) || !knows(matrix,i,cand)){
                    return -1;
                }
            }
        }
        return cand;

    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int [][]matrix=new int[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                matrix[i][j]=sc.nextInt();
            }
        }
        int celeb=findceleb(matrix, n);
        if(celeb==-1){
            System.out.println("No celebrirt");
        }
        else{
            System.out.print(celeb);
        }

    }
}