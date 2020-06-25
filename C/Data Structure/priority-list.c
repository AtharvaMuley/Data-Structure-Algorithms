#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define HIGH 3
#define MEDIUM 2
#define LOW 1


struct node{
    int val;
    int priority;
    struct node* next;
};

struct node *head = NULL;

void insert(int val, int priority){
    // Flag is unset when the element is added to its proper position
    int flag = 1;
    struct node *new_node = malloc(sizeof(struct node));
    struct node *temp, *prev;

    new_node->val = val;
    new_node->priority = priority;
    new_node->next = NULL;
    
    if (head == NULL){
        head = new_node;
        return;
    }
    else if(head->priority < priority){
        new_node->next = head;
        head = new_node;
        return;
    }
    prev = temp = head;
    while(flag != 0 && temp != NULL){

        if (temp->next == NULL && priority == temp->priority)
        {
            temp->next = new_node;
            flag = 0;
        }
        else if (priority <= temp->priority && temp->next != NULL){
            prev = temp;
            // temp->next = new_node;
            temp = temp->next;
        }
        else{
            prev->next = new_node;
            new_node->next = temp;
            flag = 0;
        }
    }
}

// Print entire list
void display(){
    struct node *temp = head;
    // printf("Head val: %d", temp->val);
    while (temp != NULL)
    {
        printf("%d -> ", temp->val);
        temp = temp->next;
    }
    printf("NULL\n");
}
int main(int argc, char const *argv[])
{
    insert(1, LOW);
    insert(1, LOW);
    insert(1, LOW);
    insert(2, MEDIUM);
    insert(2, MEDIUM);
    insert(3, HIGH);
    insert(3, HIGH);
    insert(3, HIGH);
    display();
    return 0;
}
