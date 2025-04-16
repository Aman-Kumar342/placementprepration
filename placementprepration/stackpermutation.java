import java.util.*;
public class stackpermutation{
    public static boolean isstackper(int [] input, int [] output){
        if(input.length!=output.length){
            return false;
        }
        Stack<Integer>st=new Stack<>();
        int j=0;
        for(int val:input){
            st.push(val);
            while(!st.isEmpty() && st.peek()==output[j]){
            st.pop();
            j++;
        }
        }
        return st.isEmpty();

    }
    public static void main(String[] args){
        Scanner sc=new Scanner (System.in);
        int n=sc.nextInt();
        int []arr=new int[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        int m=sc.nextInt();
        int [] arr2=new int[m];
        for(int i=0;i<n;i++){
            arr2[i]=sc.nextInt();
        }
        if(isstackper(arr, arr2)){
            System.out.println("Yes the 2nd array is permutation of the first array");
        }
        else{
            System.out.print("No the array is not the permutaion of the first array");
        }

    }
}