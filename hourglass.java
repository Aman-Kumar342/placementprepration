import java.util.*;
public class hourglass{
    public static int maxsum(int [][]mat){
        int n=mat.length;
        int m=mat[0].length;
        int maxs=Integer.MIN_VALUE;
       
        if(n<3 && m<3){
            return -1;
        }
        for(int i=0;i<n-2;i++){
            for(int j=0;j<m-2;j++){
                int sum=mat[i][j]+mat[i][j+1]+mat[i][j+2]+mat[i+1][j+1]+mat[i+2][j]+mat[i+2][j+1]+mat[i+2][j+2];
                maxs=Math.max(sum,maxs);
            }
        }
        return maxs;
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter thr row");
        int n=sc.nextInt();
        System.out.println("Enter the col");
        int m=sc.nextInt();
        int [][]mat=new int[n][m];
        System.out.println("Enter the element in matrix");
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                mat[i][j]=sc.nextInt();
            }
        }
        System.out.println("Your typed matrix is ");
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                System.out.print(mat[i][j] + " ");
            }
            System.out.println();
        }
        int res=maxsum(mat);
        System.out.println(res);

    }
}