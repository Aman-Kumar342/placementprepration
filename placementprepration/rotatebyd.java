import java.util.*;
public class rotatebyd{
    public static void rot(int []arr,int d){
        int n=arr.length;
        d=d%n;
        reverse(arr,0,d);
        reverse(arr,d+1,n-1);
        reverse(arr,0,n-1);
    } 
    public static void reverse(int []arr,int start,int end){
        while(start<end){
            int temp=arr[start];
            arr[start]=arr[end];
            arr[end]=temp;
            start++;
            end--;
        }
    }
    public static void main(String [] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int []arr= new int[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        int d=sc.nextInt();
        for(int i=0;i<n;i++){
            // System.out.print(rot())
        }
    }
}