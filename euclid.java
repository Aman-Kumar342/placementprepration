import java.util.*;
public class euclid{
    public static int find(int a,int b){
        if(b==0){
            return a;
        }
        return find(b,a%b);
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        int b=sc.nextInt();
        int c=find(a,b);
        System.out.println(c);
    }
}

