#include <iostream>
#include <string>
#include <stack>
using namespace std;

class node
{
public:
    char data;
    node *left, *right;
    node()
    {
        left = right = NULL;
    }
};

class expressiontree
{
public:
    node *root;
    expressiontree()
    {
        root = NULL;
    }
    void create(string str);
    int priority(char ch);
    void deleteTree(node *temp);
    void postorderTraversal(node *root);
};

int expressiontree ::priority(char ch)
{
    switch (ch)
    {
        case '+':
        case '-':
            return 0;
        case '*':
        case '/':
            return 1;
        case '^':
            return 2;
    }
    return -1; // Default case
}

void expressiontree ::create(string str)
{
    stack<node *> operand_st;
    stack<node *> operator_st;
    for (char ch : str)
    {
        node *temp = new node();
        temp->data = ch;
        if (isalpha(ch))
        {
            operand_st.push(temp);
        }
        else
        {
            if (operator_st.empty())
                operator_st.push(temp);
            else
            {
                while (!operator_st.empty() && priority(ch) <= priority(operator_st.top()->data))
                {
                    node *operat = operator_st.top();
                    operator_st.pop();
                    operat->right = operand_st.top();
                    operand_st.pop();
                    operat->left = operand_st.top();
                    operand_st.pop();
                    operand_st.push(operat);
                }
                operator_st.push(temp);
            }
        }
    }
    while (!operator_st.empty())
    {
        node *operat = operator_st.top();
        operator_st.pop();
        operat->right = operand_st.top();
        operand_st.pop();
        operat->left = operand_st.top();
        operand_st.pop();
        operand_st.push(operat);
    }
    root = operand_st.top();
}

void expressiontree ::deleteTree(node *temp)
{
    if (temp == NULL)
        return;

    deleteTree(temp->left);
    deleteTree(temp->right);
    delete temp;
}

void expressiontree ::postorderTraversal(node *root)
{
    if (root == NULL)
        return;

    postorderTraversal(root->left);
    postorderTraversal(root->right);
    cout << root->data << " ";
}

int main()
{
    expressiontree e;
    string str;
    int ch;

    do
    {
        cout << "\n Enter Choice: ";
        cout << "\n\t1.Create expression tree \n\t2.Postorder Traversal \n\t3.Delete tree \n\t4.Exit";
        cout << "\n Choice: ";
        cin >> ch;

        switch (ch)
        {
            case 1:
                cout << "Enter Expression : ";
                cin >> str;
                e.create(str);
                break;
            case 2:
                if (e.root == NULL)
                {
                    cout << "Expression tree is empty." << endl;
                }
                else
                {
                    cout << "Postorder Traversal: ";
                    e.postorderTraversal(e.root);
                    cout << endl;
                }
                break;
            case 3:
                e.deleteTree(e.root);
                e.root = NULL;
                cout << "Expression tree deleted." << endl;
                break;
            case 4:
                break;
        }
    } while (ch != 4);

    return 0;
}
