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

class Codec {
private:
    TreeNode* dfs(size_t& i, const vector<string>& nodes) {
        if (nodes[i] == "N") {
            i++;
            return nullptr;
        }

        TreeNode* node = new TreeNode(stoi(nodes[i]));
        i++;
        node->left = dfs(i, nodes);
        node->right = dfs(i, nodes);
        return node;
    }

public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (root == nullptr) return "N";

        string result = to_string(root->val);
        stack<TreeNode*> s;
        s.push(root->right);
        s.push(root->left);
        while (!s.empty()) {
            auto node = s.top();
            s.pop();
            if (node == nullptr) {
                result += ",N";
            } else {
                result += "," + to_string(node->val);
                s.push(node->right);
                s.push(node->left);
            }
        }

        return result;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        stringstream ss(data);
        vector<string> nodes;
        string node;
        while (getline(ss, node, ',')) {
            nodes.push_back(node);
        }
        size_t i = 0;
        return dfs(i, nodes);
    }
};


// "1,2,N,N,3,4,N,N,5,N,N"