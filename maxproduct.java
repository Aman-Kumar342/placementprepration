// import java.util.*;
// public class maxproduct{
//     public static int maxp(int[]arr){
//         int n=arr.length;
//         int maxpr=Integer.MIN_VALUE;
//         for(int i=0;i<n;i++){
//             for(int j=i;j<n;j++){
//                 int product=1;
//                 for(int k=i;k<=j;k++){
//                     product=product*arr[k];
//                 }
//                 maxpr=Math.max(maxpr,product);
//             }
//         }
//         return  maxpr;
//     }
//     public static void main(String[] args) {
//         Scanner sc=new Scanner(System.in);
//         System.out.println("Enter the number of array size");
//         int n=sc.nextInt();
//          int[] arr = new int[n];
//         System.out.println("ENter the array element");
//         for(int i=0;i<n;i++){
//             arr[i]=sc.nextInt();
//         }
//         int res=maxp(arr);
//         System.out.println(res);
//     }
// }

import java.util.*;
public class maxproduct{
    public static int maxprod(int[] arr){
        int n=arr.length;
        int maxprd=Integer.MIN_VALUE;
        for(int i=0;i<n;i++){
            int product=1;
            for(int j=i;j<n;j++){
                product=product*arr[j];
                maxprd=Math.max(maxprd,product);
            }
        }
        return maxprd;
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the value of n");
        int n=sc.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        int res=maxprod(arr);
        System.out.println(res);
    }
}
