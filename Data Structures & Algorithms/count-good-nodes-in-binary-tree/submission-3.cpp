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
    int dfs(TreeNode* node, int max_val) {
        if (node == nullptr) return 0;

        int is_good = node->val >= max_val ? 1 : 0;
        return (
            is_good + 
            dfs(node->left, max(max_val, node->val)) + 
            dfs(node->right, max(max_val, node->val))
        );
    }

public:
    int goodNodes(TreeNode* root) {
        return dfs(root, numeric_limits<int>::min());
    }
};
