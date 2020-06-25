#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int val;
    struct Node *leftChild;
    struct Node *rightChild;
}TreeNode;

TreeNode *root = NULL;

void insert(int val){
    TreeNode *new_node = malloc(sizeof(TreeNode));
    new_node->val = val;
    new_node->leftChild = NULL;
    new_node->rightChild = NULL;

    if(root == NULL){
        root = new_node;
        return;
    }

    TreeNode *current = root; 
    while (1)
    {
        //If value is smaller than the current traverse to left Subtree
        if(current->val > val){
            if(current->leftChild == NULL){
                current->leftChild = new_node;
                return;
            }
            current = current->leftChild;
        }
        //If value is greater than the current traverse to left Subtree
        else{

            if(current->rightChild == NULL){
                current->rightChild = new_node;
                return;
            }
            current = current->rightChild;
        }
    }
}
// Inorder Traversal
void inorder(TreeNode *current){
    if(current == NULL){
        return;
    }
    inorder(current->leftChild);
    printf(" %d", current->val);
    inorder(current->rightChild);
    if (current == root)
        printf("\n");
}

// Post Order Traversal
void post_order(TreeNode *current){
    if(current == NULL){
        return;
    }
    post_order(current->leftChild);
    post_order(current->rightChild);
    printf(" %d", current->val);
    if (current == root)
        printf("\n");
}

// Pre Order Traversal
void pre_order(TreeNode *current){
    if(current == NULL){
        return;
    }
    printf(" %d", current->val);
    pre_order(current->leftChild);
    pre_order(current->rightChild);
    if (current == root)
        printf("\n");
}

// Search Item in Binary Tree
void search(int val){
    if(root == NULL){
        printf("No data in Tree\n");
        return;
    }
    TreeNode *current = root;
    while (1){
        // If value is smaller than the current traverse to left Subtree
        if(current == NULL){
            printf("Item: %d not found\n", val);
            return;
        }
        if(current->val == val){
            printf("Item: %d found\n", val);
            return;
        }
        if(current->val < val){
            current = current->leftChild;
        }
        // If value is smaller than the current traverse to right Subtree
        else{
            current = current->rightChild;
        }
    }
}

int main(int argc, char const *argv[])
{
    insert(27);
    insert(14);
    insert(35);
    insert(10);
    insert(19);
    insert(31);
    insert(42);
    printf("In Order  : ");
    inorder(root);
    printf("Pre Order : ");
    pre_order(root);
    printf("Post Order: ");
    post_order(root);
    return 0;
}