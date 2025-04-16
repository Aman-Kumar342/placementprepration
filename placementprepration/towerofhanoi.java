import java.util.*;
public class towerofhanoi{
    public static void toh(int n, char src, char aux, char dest){
        if(n==1){
            System.out.println("Move disk 1 from " + src + " to " + dest);
            return ;
        }
        toh(n-1,src,dest,aux);
        System.out.println("Move disk " + n + " from " + src + " to " + dest);
        toh(n-1,aux,src,dest);
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        toh(n,'a','b','c');
    }

}