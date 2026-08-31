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
    int dfs(TreeNode* node, int& max_path_sum) {
        if (node == nullptr) return 0;

        int max_left = dfs(node->left, max_path_sum);
        int max_right = dfs(node->right, max_path_sum);

        max_path_sum = max(max_path_sum, max_left + max_right + node->val);

        return max(0, node->val + max(max_left, max_right));
    }

public:
    int maxPathSum(TreeNode* root) {
        if (root == nullptr) return 0;

        int max_path_sum = root->val;
        dfs(root, max_path_sum);
        return max_path_sum;
    }
};
