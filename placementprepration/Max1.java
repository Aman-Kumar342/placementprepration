import java.util.*;
public class Max1{
    public static int max_one(int n){
        String Binarys=Integer.toBinaryString(n);
        int maxcount=0;
        int count=0;
        for(char digit: Binarys.toCharArray()){
            if(digit=='1'){
                count++;
            }
            if(count>maxcount){
                maxcount=count;
            }
            else{
                count=0;
            }
        }
        return maxcount;
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number");
        int n=sc.nextInt();
        System.out.print("the maximum 1 is"+ n);

    }
}
