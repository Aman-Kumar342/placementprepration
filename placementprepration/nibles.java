import java.util.*;
public class nibles{
    public static int number(int n){
        int right=n&15;
        right=right<<4;
        int left=n>>4;
        return (right|left);

    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the value of n");
        int n=sc.nextInt();
        int res=number(n);
        System.out.print(res);

        
    }
}
