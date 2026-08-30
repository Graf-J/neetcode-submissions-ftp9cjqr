/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
private:
    int dfs(TreeNode* node, int& max_diameter) {
        if (node == nullptr) return 0;

        int depth_left = dfs(node->left, max_diameter);
        int depth_right = dfs(node->right, max_diameter);

        max_diameter = max(max_diameter, depth_left + depth_right);

        return 1 + max(depth_left, depth_right);
    }

public:
    int diameterOfBinaryTree(TreeNode* root) {
        int max_diameter = 0;
        dfs(root, max_diameter);
        return max_diameter;
    }
};
