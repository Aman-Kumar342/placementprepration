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

public class leftview{

    void reversepre(TreeNode root, int level, List<Integer> ans){
        if(root==null){
            return;
        }
        if(ans.size()==level){
            ans.add(root.val);
        }
        reversepre(root.left,level+1,ans);
        reversepre(root.right,level+1,ans);
    }
    public List<Integer>leftvi(TreeNode root){
        List<Integer>ans=new ArrayList<>();
        reversepre(root, 0, ans);
        return ans;
    }
}