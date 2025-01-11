import java.util.*;
public class equilibsum{
    public static int equilib(int [] arr){
        int n=arr.length;
        int totalsum=0;
        int leftsum=0;
        int maxsum=Integer.MIN_VALUE;
        for(int i=0;i<n;i++){
            totalsum+=arr[i];
        }
        for(int i=0;i<n;i++){
            totalsum=totalsum-arr[i];
            if(leftsum==totalsum){
                maxsum=Math.max(leftsum,maxsum);
            }
            leftsum+=arr[i];
        }
        return maxsum;
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int [] arr=new int[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        int res=equilib(arr);
        System.out.println(res);
    }
}
