// import java.util.*;
// public class prime{
//     public static void main(String[] args) {
//         Scanner sc=new Scanner(System.in);
//         int n=sc.nextInt();
//         int [] numarr=new int[n+1];
//         for(int i=2;i<=n;i++){
//             numarr[i]=1;
//         }
//         for(int i=2;i*i<=n;i++){
//             if(numarr[i]==1){
//                 for(int j=i*i;j<n;j+=i){
//                     numarr[j]=0;
//                 }
//             }
//         }
//         System.out.println("Printing the prime n");
//         for(int i=2;i<=n;i++){
//             if(numarr[i]==1){
//                 System.out.print(i+" ");
//             }
//         } 
//     }
// }
import java.util.*;
public class prime{
    public static boolean isprime(int n){
        if(n<1){
            return false;
        }
        for(int i=2;i*i<n;i++){
            if(n%i==0){
                return false;
            }
        }
        return true;

    }
    public static void printprime(int limit){
        for(int i=2;i<=limit;i++){
            if(isprime(i)){
                System.out.print (i + " ");
            }
        }
    }
    public static void main(String [] args){
        Scanner sc=new Scanner(System.in);
        int limit=sc.nextInt();
        printprime(limit);
    }
}
