import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;
public class sortingofqueue{
    public static Queue<Integer> sortQueue(Queue<Integer>queue){
        List<Integer> list=new ArrayList<>(queue);
        Collections.sort(list);
        Queue<Integer> sortedQueue=new LinkedList<>(list);
        return sortedQueue;
    }
    public static void main(String[] args){
        Queue<Integer>queue=new LinkedList<>();
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        for(int i=0;i<n;i++){
            queue.add(sc.nextInt());
        }
        Queue<Integer>sortqw=sortQueue(queue);
        System.out.print("ans :" +sortqw);
    }
}