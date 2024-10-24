class Solution {
    public boolean flipEquiv(TreeNode root1, TreeNode root2) {
        return mine(root1, root2);
    }

    private boolean mine(TreeNode root1, TreeNode root2) {
        if (root1 == null && root2 == null) {
            return true;
        }

        if (root1 == null || root2 == null) {
            return false;
        }

        if (root1.val != root2.val) {
            return false;
        }

        boolean flip = true;
        boolean noFlip = true;

        noFlip &= mine(root1.left, root2.left);
        noFlip &= mine(root1.right, root2.right);

        flip &= mine(root1.left, root2.right);
        flip &= mine(root1.right, root2.left);

        return noFlip || flip;
    }

    
}
