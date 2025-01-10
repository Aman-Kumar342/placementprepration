import java.util.*;
public class binarypalindr{
    public static boolean ispalindrome(int n){
        String Binarysring=Integer.toBinaryString(n);
        int left=0;
        int right=Binarysring.length()-1;
        while(left<right){
            if(Binarysring.charAt(left)!=Binarysring.charAt(right)){
                return false;
            }
            left++;
            right--;
        }
        return true;


    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number");
        int n=sc.nextInt();
        if(ispalindrome(n)){
            System.out.println("it is a palindrom");

        }
        else{
            System.out.println("It sis not a palindrome");
        }
        
    }
}
