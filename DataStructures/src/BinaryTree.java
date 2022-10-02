import java.awt.*;
import java.net.StandardSocketOptions;
import java.util.*;
public class BinaryTree {

    private TreeNode root;

    public class TreeNode{
        private TreeNode left;
        private TreeNode right;
        private int data;

        public TreeNode(int data){
            this.data= data;
        }

    }

    public void CreateBinaryTree(){
        TreeNode first = new TreeNode(9);
        TreeNode second = new TreeNode(2);
        TreeNode third = new TreeNode(3);
        TreeNode fourth = new TreeNode(4);

        root = first;
        root.left=second;
        root.right=third;
        second.left=fourth;




    }

    public void preOrder(TreeNode root){
        if(root==null){
            return;
        }
        System.out.println(root.data + " ");
        preOrder(root.left);
        preOrder(root.right);
    }

    public void preOrderIterative(){
        if(root== null){
            return;
        }

        Stack<TreeNode> st = new Stack<>();
        st.push(root);
        while(!st.isEmpty()){
            TreeNode temp = st.pop();
            System.out.println(temp.data + " ");
            if(temp.right!=null){
                st.push(temp.right);
            }
            if(temp.left!=null){
                st.push(temp.left);
            }
        }
    }

    public static void main(String[] args) {
        BinaryTree bt = new BinaryTree();
        bt.CreateBinaryTree();
        bt.preOrderIterative();

    }

}
