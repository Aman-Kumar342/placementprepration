import java.util.*;
class TreeNode{
    int val;
    TreeNode left, right;
    TreeNode(int val){
        this.val=val;
        this.left=null;
        this.right=null;
    }
}
public class boundrytraversal{
    public static Boolean isleaf(TreeNode root){
        return(root !=null && root.left!=null && root.right!=null);
    }
    public void addleft(TreeNode root, List<Integer> ans){
        TreeNode temp=root.left;
        while(temp!=null){
             if(!isleaf(temp)){
                ans.add(temp.val);
             }
             if(temp.left!=null){
                temp=temp.left;
             }
             else{
                temp=temp.right;
             }
        }

    }
    public void addleaf(TreeNode root, List<Integer>ans){
        if(root!=null){
            return;
        }
        if(isleaf(root)){
            ans.add(root.val);
            return;
        }
        addleaf(root.left, ans);
        addleaf(root.right, ans);

    }
    public void addright(TreeNode root, List<Integer>ans){
        TreeNode temp=root.right;
        List<Integer>tempres=new ArrayList<>();
        while(temp!=null){
            if(!isleaf(temp)){
                tempres.add(temp.val);
            }
            if(temp.right!=null){
                temp=temp.right;
            }
            else {
                temp=temp.left;
            }
        }
    }

    public List<Integer>boundry(TreeNode root){
        List<Integer>res=new ArrayList<>();
        if(root==null){
            return res;
        }
        if(!isleaf(root)){
            res.add(root.val);
        }
        addleft(root, res);
        addleaf(root, res);
        addleft(root,res);
        return res;

    }

}