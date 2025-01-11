import java.util.*;
public class karatbusha{
    public static long mul(long x,long y){
        if(x<10|| y<10){
            return x*y;
        }
        int n=Math.max(Long.toString(x).length() , Long.toString(y).length());
        int half=n/2;
        long a = x / (long) Math.pow(10, half);
        long b = x % (long) Math.pow(10, half);
        long c = y / (long) Math.pow(10, half);
        long d = y % (long) Math.pow(10, half);
        
        long ac=mul(a,c);
        long bd=mul(b,d);
        long ad_plus_bc=mul(a+b,c+d)-ac-bd;

        return ac*(long)Math.pow(10,2*half)+ad_plus_bc*(long)Math.pow(10,half)+bd;
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number");
        long x=sc.nextLong();

        System.out.println("ENter the 2nd number");
        long y=sc.nextLong();

        long result=mul(x,y);
        System.out.print(result);

    }
}

