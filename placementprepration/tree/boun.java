import java.awt.image.RescaleOp;
import java.util.*;
import javax.swing.event.AncestorEvent;
class TreeNode{
    int data;
    TreeNode left, right;
    TreeNode(int val){
        this.data=val;
        this.left=null;
        this.right=null;
    }
    public class Binarytraversal{
        static Scanner sc=new Scanner(System.in);
        public static boolean isLeaf(Node root){
            return (root!=null && root.left==null&& root.right==null);

        }
        public static void addleft(TreeNode root ,List<Integer>res){
            TreeNode temp=root.left;
            while(temp!=null){
                if(!isleaf(temp)){
                    res.add(temp.data);
                }
                if(temp.left!=null){
                    temp=temp.left;
                }
                else{
                    temp=temp.right;
                }
            }
        }
        public static void addright(TreeNode root, List<Integer>res){
            TreeNode temp=root.right;
            List<Integer>tempres=new ArrayList<>();
            while(temp!=null){
                if(!isLeaf(temp)){
                    tempres.add(temp.data);
                }
                if(temp.right!=null){
                    temp=temp.right;
                }
                else{
                    temp=temp.left;
                }
                Collections.reverse(tempres);
                res.addAll(tempres);
            }
        }
        public static void addleaf(TreeNode root, List<Integer>res){
            if(root==null){
                return;
            }
            if(isleaf(root)){
                res.add(root.data);
                return;
            }
            addleaf(root.left,res);
            addleaf(root.right,res);
        }
        public static List<Integer>bound(TreeNode root){
            List<Integer>ans=new ArrayList<>();
            if(root==null){
                return ans;
            }
            if(!isleaf(root)){
                ans.add(root.data);
            }
        }
    }
}