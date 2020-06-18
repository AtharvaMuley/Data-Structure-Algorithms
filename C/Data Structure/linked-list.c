#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

struct node
{
    int val;
    struct node *next;
};

struct node *head;
struct node *tail;

void init(){
    head = NULL;
    tail = NULL;
}
void insert_element(int val){
    struct node *new_node;
    new_node = (struct node*) malloc(sizeof(struct node));
    new_node->val = val;
    new_node->next = NULL;
   
    if (head == NULL){
        head = new_node;
        tail = new_node;
        return;
    }
    else
    {
        tail->next = new_node;
        tail = new_node;
    }
}

// Removes first occurence of the element
void remove_element(int val){
    struct node *temp = head;
    struct node *prev = head;

    if(temp == NULL){
        printf("List is empty\n");
        return;
    }
    while (temp != NULL){
        if (temp->val == val && temp == head){
            head = head->next;
            free(temp);
            return;
        }
        else if (temp->val == val && temp != head)
        {
            prev->next = temp->next;
            free(temp);
            return;
        }
        else{
            prev = temp;
            temp = temp->next;
        }
    }
}

void print_list(){
    struct node* temp = head;
    while (temp != NULL)
    {
        printf("%d, ", temp->val);
        temp = temp->next;
    }
    printf("\n");
}

int main(int argc, char const *argv[])
{
    init();
    remove_element(4);
    insert_element(4);
    insert_element(3);
    insert_element(2);
    insert_element(1);
    remove_element(4);
    print_list();
    return 0;
}
