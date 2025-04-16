import java.util.*;
class TreeNode{
    int val;
    TreeNode left, right;
    TreeNode(int val){
        this.val=val;
        this.left=null;
        this.right=null;
    }
    public class replacebst{
        public void ino(TreeNode root, List<Integer> vals){
            if(root==null){
                retrun;
            }
            ino(root.left, vals);
            vals.add(root.val);
            ino(root.right,vals);

        }
        public void rep(TreeNode root, List<Integer>vals , int index){
            if(root==null){
                return;
            }
            rep(root.left,vals,index);
            root.val = vals.get(index[0]++);
            rep(root.right,vals,index);
        }
        public void recover(TreeNode root){
            if(root==null){
                return;
            }
            List<Integer>vals=new ArrayList<>();
            ino(root,vals);
            Collections.sort(val);
            int [] index={0};
            rep(root,vals,index);

        }
    }
}