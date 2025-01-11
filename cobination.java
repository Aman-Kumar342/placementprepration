import java.util.*;
public class cobination{
    public static int fact(int n){
        if(n==0 || n==1){
            return 1;
        }
        return n*fact(n-1);
    }
    public static int calc(int n,int r){
        return fact(n)/fact(r)*fact(n-r);
    }
    public static void main(String [] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int r=sc.nextInt();
        if(r>n || r<0){
            System.out.println("Invalid input");
        }
        else{
            int res=calc(n,r);
            System.out.print(res);
        }
    }

}