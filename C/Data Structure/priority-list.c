#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define HIGH 1
#define MEDIUM 2
#define LOW 3


struct node{
    int val;
    int priority;
    struct node* next;
};

struct node *head = NULL;

void insert(int val, int priority){
    struct node * new_node = malloc(sizeof(struct node));
    new_node->val = val;
    new_node->priority = priority;
    new_node->next = NULL;
    
    if (head == NULL){
        head = new_node;
    }
}

int main(int argc, char const *argv[])
{
    
    return 0;
}
