import java.util.*;
public class view{
    class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int val){
            this.val=val;
            this.right=null;
            this.left=null;
        }

    }
   static class Pair {
        TreeNode node;
        int line;
        
        Pair(TreeNode node, int line) {
            this.node = node;
            this.line = line;
        }
    }
    private static void reversepred(TreeNode root, int level, List<Integer>ans){
        if(root==null){
            return;
        }
        if(ans.size()==level){
            ans.add(root.val);
        }
    
    }
    private static void reversepre(TreeNode root, int level,List<integer>ans){
        if(root==null){
            return;
        }
        if(ans.size()==level){
            ans.add(root.val);
        }
        reversepre(root.left, level+1,ans);
        reversepre(root.right, level+1, ans);
    }
    public static List<Integer>leftv(TreeNode root){
        List<Integer>ans=new ArrayList<>();
        reversepre(root, 0, ans);
        return ans;
    }
    public static List<Integer>topview(TreeNode root){
        List<Integer>ans=new ArrayList<>();
        if(root==null){
            return ans;
        }
        Map<Integer, Integer>mp=new TreeMap<>();
        Queue<Pair>q=new LinkedList<>();
        q.add(new Pair(root, 0));
        while(!q.isEmpty()){
            Pair temp=q.poll();
            TreeNode node=temp.node;
            int line=temp.line;
            if(!mp.containsKey(line)){
                mp.put(line, node.val);
            }
            if(node.left!=null){
                q.add(new Pair(node.left,line-1));
            }
            if(node.right!=null){
                q.add(new Pair(node.right,line+1));
            }
        }
        for(int value : mp.values()()){
            ans.add(value);
        }
        return ans;
    }
    public static List<Integer>bottomv(TreeNode root)









}