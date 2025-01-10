import java.util.*;
public class armstrong{
    public static void main(String[] args) {
        System.out.println("Enter the number");
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int digits=0;
        while(n!=0){
            n/=10;
            digits++;
        }
        int sum=0;
        while(n!=0){
            int digit=n%10;
            sum+=Math.pow(digit,digits);
            n/=10;
        }
        if(sum==n){
            System.out.println("It is a armstrong ");
        }
        else{
            System.out.println("Not a");
        }
        

        
    }
}
