import java.util.*;
import java.io.*;
class TreeNode{
    int val;
    TreeNode left, right;
    TreeNode(int val){
        this.val=val;
        this.left=null;
        this.right=null;
    }
}
public class bottomview{
    static class Pair {
        TreeNode node;
        int line;
        
        Pair(TreeNode node, int line) {
            this.node = node;
            this.line = line;
        }
    }
    public List<Integer> bottomv (TreeNode root){
        List<Integer>ans=new ArrayList<>();
        if(root==null){
            return ans;
        }
        Map<Integer, Integer>mpp=new TreeMap<>();
      
        Queue<Pair>q=new LinkedList<>();
        q.add(new Pair(root, 0));
        while(!q.isEmpty()){
            Pair temp=q.poll();
            TreeNode node=temp.node;
            int line=temp.line;
            mpp.put(line,node.val);
             if(node.left != null) {
                q.add(new Pair(node.left, line - 1));
            }
            if(node.right != null) {
                q.add(new Pair(node.right, line + 1));
            }
        }
        for(int value:mpp.values()){
            ans.add(value);
        }
        return ans;

    }
}