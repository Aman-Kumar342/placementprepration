import java.util.*;
import javax.xml.transform.Templates;
public class check{
    class TreeNode{
        int val;
        TreeNode left, right;
        TreeNode(int val){
            this.val=val;
            this.left=null;
            this.right=null;

        }
    }
    class Pair{
        TreeNode node;
        int line;
        Pair(TreeNode node, int line){
            this.node=node;
            this.line=line;
        }
    }
    public static List<Integer>bottomview(TreeNode root){
        List<Integer>ans=new ArrayList<>();
        if(root==null){
            return ans; 
        }
        Map<Integer, Integer>mp=new TreeMap<>();
        Queue<Pair>q=new LinkedList<>();
        q.add(new Pair(root,0));
        while(!q.isEmpty()){
            Pair temp=q.poll();
            TreeNode node=temp.node;
            int line=Templates.line;
            if(!mp.Cont)


        }
    }
}