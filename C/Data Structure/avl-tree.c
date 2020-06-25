#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    int val;
    struct node *leftSubtree;
    struct node *rightSubtree;
    int height;
}TreeNode;

TreeNode *root = NULL;

int Height(TreeNode *node){
    if(node == NULL)
        return 0;
    else
        return node->height;
}

int max(int val1, int val2){
    return val1 > val2 ? val1 : val2;
}

int getBalanceFactor(TreeNode *node){
    if(node == NULL)
        return 0;
    else
        return Height(node->leftSubtree) - Height(node->rightSubtree);
}

TreeNode* leftRotate(TreeNode *node){
    /*
        node is the current passed from insert
    */
   TreeNode* y = node->rightSubtree;
   TreeNode* T2 = y->leftSubtree;

   //Perform rotations
   node->rightSubtree = T2;
   y->leftSubtree = node;
   
   // Updates the height of Trees
   y->height = max(Height(y->leftSubtree), Height(y->rightSubtree));
   node->height = max(Height(node->leftSubtree), Height(node->rightSubtree));

   return y;
}

TreeNode* rightRotate(TreeNode *node){
    /*
        node is the current passed from insert
    */
   TreeNode* y = node->leftSubtree;
   TreeNode* T3 = y->rightSubtree;

   //Perform rotations
   node->leftSubtree = T3;
   y->rightSubtree = node;

   // Updates the height of Trees
   y->height = max(Height(y->leftSubtree), Height(y->rightSubtree));
   node->height = max(Height(node->leftSubtree), Height(node->rightSubtree));
   
   return y;
}

TreeNode* insert(TreeNode *current, int val){
    // Create new tree node
    TreeNode *new_node = (TreeNode*) malloc(sizeof(TreeNode));
    new_node->val = val;
    new_node->leftSubtree = NULL;
    new_node->rightSubtree = NULL;
    new_node->height = 1;

    //Check if Tree is Null (ie not initialized)
    if (current == NULL){
        return new_node;
    }
    // else
    if(val < current->val)
        current->leftSubtree = insert(current->leftSubtree, val);
    else if(val > current->val)
        current->rightSubtree = insert(current->rightSubtree, val);
    // Duplicate values cannot be inserted into BST
    else
        return current;

    //Update the height of this node
    current->height = 1 + max(Height(current->leftSubtree), Height(current->rightSubtree));

    int balance = getBalanceFactor(current);

    // Left-Left case
    if(balance > 1 && val < current->leftSubtree->val)
        return rightRotate(current);
    
    // Left-Right case
    else if(balance > 1 && val > current->leftSubtree->val){
        current->leftSubtree =leftRotate(current->leftSubtree);
        return rightRotate(current);
    }

    //Right-Right case
    else if(balance < -1 && val > current->rightSubtree->val)
        return leftRotate(current);
    
    //Right-Left case
    else if(balance < -1 && val < current->rightSubtree->val){
        current->rightSubtree = rightRotate(current->rightSubtree);
        return leftRotate(current);
    }
    else
        return current;

}

void preorder(TreeNode* node){
    if(node==NULL)
        return;
    printf("%d ", node->val);
    preorder(node->leftSubtree);
    preorder(node->rightSubtree);
    if(node == root)
        printf("\n");
}

int main(int argc, char const *argv[])
{
    root = insert(root, 40); 
    root = insert(root, 30); 
    root = insert(root, 20); 
    root = insert(root, 10); 
    root = insert(root, 50); 
    root = insert(root, 25);
    preorder(root);
    return 0;
}
