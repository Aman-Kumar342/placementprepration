import java.util.*;
class TreeNode{
    int val;
    TreeNode left,right;
    TreeNode(int val){
        this.val=val;
        this.left=null;
        this.right=null;
    }
}
public class swapbst{
    public static void inorder(TreeNode root, List<Integer> vals){
        if(root==null){
            return ;
        }
        inorder(root.left, vals);
        vals.add(root.val);
        inorder(root.right,vals);
    }
    public static void replacewithorted(TreeNode root, List<Integer>vals, int [] index){
        if(root==null){
            return;
        }
        replacewithorted(root.left, vals, index);
        root.val=vals.get(index[0]++);
        replacewithorted(root.right, vals, index);
    }
    public static void recoverbst(TreeNode root){
        List<Integer>vals=new ArrayList<>();
        inorder(root,vals);
        Collections.sort(vals);
        int[] index={0};
        replacewithorted(root, vals, index);
    }
}