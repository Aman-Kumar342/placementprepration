import java.util.*;
public class equlib{
    public static int[] index(int [] arr){
        int n=arr.length;
        ArrayList<Integer>ans = new ArrayList<>();
        for(int i=0;i<n;i++){
            boolean isleader=true;
            for(int j=i+1;j<n;j++){
                if(arr[j]>arr[i]){
                    isleader=false;
                    break;
                }
            }
            if(isleader){
                ans.add(arr[i]);
            }
        }
        int [] lArr=new int[ans.size()];
        for(int i=0;i<ans.size();i++){
            lArr[i]=ans.get(i);
        }
        return lArr;
    }
    public static int maxn(int [] arr){
        int n=arr.length;
        int max=arr[0];
        for(int i=1;i<n;i++){
            if(arr[i]>max){
                max=arr[i];
            }
            return max;
        }
        return 0;

    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the size of array");
        int n=sc.nextInt();
        int [] arr=new int[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
     int [] newl=index(arr);
     int res=maxn(newl);
     System.out.println(res);
    }
}