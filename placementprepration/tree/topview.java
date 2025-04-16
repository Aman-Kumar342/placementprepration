import java.io.*;
import java.util.*;
import org.w3c.dom.Node;
class TreeNode{
    int val;
    TreeNode left, right;
    TreeNode(int val){
        this.val=val;
        this.right=null;
        this.left=null;
    }
}
public class topview{
    public class Pair{
        TreeNode node;
        int line;
        Pair(TreeNode node, int line){
            this.node=node;
            this.line=line;
        }
    }
    public List<Integer> Topviewtree(TreeNode root){
        List<Integer>ans=new ArrayList<>();
        if(root==null){
            return ans;
        }
        Map<Integer, Integer>mpp=new TreeMap<>();
        Queue<Pair>q=new LinkedList<>();
        q.add(new Pair(root,0));
        while(!q.isEmpty()){
            Pair temp=q.poll();
            TreeNode node=temp.node;
            int line=temp.line;
            if(!mpp.containsKey(line)){
                mpp.put(line,node.val);
            }
            if(node.left!=null){
                q.add(new Pair(node.left,line-1));
            }
            if(node.right!=null){
                q.add(new Pair(node.right,line+1));
            }
        }
        for(int it:mpp.values()){
            ans.add(it);
        }
        return ans;

    }
}