import java.util.Scanner;
public class strobogramtic{
    public static boolean isstro(int num){
        String nums=Integer.toString(num);
        int left=0;
        int right=nums.length()-1;
        while(left<right){
            char leftchar=nums.charAt(left);
            char rightchar=nums.charAt(right);
            if (!((leftchar=='0' && rightchar=='0')||
            (leftchar=='1' && rightchar=='1')||
            (leftchar=='6' && rightchar=='9')||
            (leftchar=='9' && rightchar=='6')||
            (leftchar=='8' && rightchar=='8'))){
                return false;
            }
            left++;
            right--;
           
        }
        return true;

    }
    public static void main(String [] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        if(isstro(n)){
            System.out.print("Yes");
        }
        else{
            System.out.println("No");
        }

    }
}
