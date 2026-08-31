struct PrefixNode {
    unordered_map<char, PrefixNode*> children;
    bool is_end;

    PrefixNode() : is_end(0) {}
};

class PrefixTree {
private:
    PrefixNode* root = new PrefixNode();

public:
    PrefixTree() {
        
    }
    
    void insert(string word) {
        PrefixNode* current = root;
        for (const auto& c : word) {
            if (!current->children.contains(c)) {
                current->children[c] = new PrefixNode();
            }
            current = current->children[c];
        }
        current->is_end = true;
    }
    
    bool search(string word) {
        PrefixNode* current = root;
        for (const auto& c : word) {
            if (!current->children.contains(c)) {
                return false;
            }
            current = current->children[c];
        }
        return current->is_end;
    }
    
    bool startsWith(string prefix) {
        PrefixNode* current = root;
        for (const auto& c : prefix) {
            if (!current->children.contains(c)) {
                return false;
            }
            current = current->children[c];
        }
        return true;
    }
};
