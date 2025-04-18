import java.util.*;
public class heapsort{

    public static void heapsortas(int [] arr){
        int n=arr.length;
        // buid max heap
        for(int i=n/2-1;i>=0;i--){
            maxheapfy(arr,n,i);

        }
        // extract elemnt
        for(int i=n-1;i>0;i--){
            swap(arr,0,i);
            maxheapfy(arr,i,0);
        }

    }
    private static void maxheapfy(int [] arr, int n, int i){
        int largest=i;
        int left=2*i+1;
        int right=2*1+2;

        if(left < n && arr[left]> arr[largest]){
            largest=left;
        }
        if(right<n && arr[right]>arr[largest]){
            largest=right;
        }
        if(largest!=i){
            swap(arr,i,largest);
            maxheapfy(arr, n, largest);
        }
    }
    public static void heapsortdec(int [] arr){
        int n=arr.length;
        for(int i=n/2-1;i>=0;i--){
            minheapfy(arr,n,i);
        }

        for(int i=n-1;i>0;i--){
            swap(arr,0,i);
            minheapfy(arr, i, 0);
        }
    }
    private static void swap(int [] arr, int i, int j){
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    }
    private static void minheapfy(int [] arr, int n, int i){
        int smallest=i;
        int left=2*i+1;
        int right=2*i+2;

        if(left<n && arr[left]< arr[smallest]){
            smallest=left;
        }
        if(right< n && arr[right]<arr[smallest]){
            smallest=right;
        }
        if(smallest !=i){
            swap(arr,i,smallest);
            minheapfy(arr, n, smallest);
        }

    }
    public static void main(String [] args){
        int [] arr={10,3,5,8,2,7,4,9,1,6};

    

    }
}