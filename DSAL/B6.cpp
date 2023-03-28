#include<iostream>
#include<stack>
#include<string>

using namespace std;

// Structure to represent a node in the expression tree
struct TreeNode {
    char val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(char x) : val(x), left(nullptr), right(nullptr) {}
};

// Function to construct the expression tree from the given expression
TreeNode* buildExpressionTree(string expression) {
    stack<TreeNode*> st;
    for(int i = 0; i < expression.length(); i++) {
        if(expression[i] == ' ') {
            continue;
        }
        if(expression[i] >= '0' && expression[i] <= '9' || isalpha(expression[i])) {
            TreeNode* node = new TreeNode(expression[i]);
            st.push(node);
        } else {
            TreeNode* right = st.top();
            st.pop();
            TreeNode* left = st.top();
            st.pop();
            TreeNode* node = new TreeNode(expression[i]);
            node->left = left;
            node->right = right;
            st.push(node);
        }
    }
    return st.top();
}

// Function to traverse the expression tree using postorder traversal (non-recursive)
void postorderTraversal(TreeNode* root) {
    stack<TreeNode*> st1, st2;
    st1.push(root);
    while(!st1.empty()) {
        TreeNode* node = st1.top();
        st1.pop();
        st2.push(node);
        if(node->left != nullptr) {
            st1.push(node->left);
        }
        if(node->right != nullptr) {
            st1.push(node->right);
        }
    }
    while(!st2.empty()) {
        cout << st2.top()->val << " ";
        st2.pop();
    }
}

// Function to delete the entire expression tree
void deleteTree(TreeNode* root) {
    if(root == nullptr) {
        return;
    }
    deleteTree(root->left);
    deleteTree(root->right);
    delete root;
}

// Main function to test the code
int main() {
    string expression = "a - b * c - d / e + f";
    TreeNode* root = buildExpressionTree(expression);
    cout << "Postorder traversal: ";
    postorderTraversal(root);
    cout << endl;
    deleteTree(root);
    return 0;
}
