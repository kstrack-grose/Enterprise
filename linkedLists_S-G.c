/*
 * Linked List Repertoire
 * Kiri Strack-Grose
 * 22.10.2014
*/

//header files
#include <stdlib.h>
#include <stdio.h>

//NODE STRUCT
typedef struct node {
 	int data;
	struct node* next;
} Node, *NodePtr;



//BEGIN THE FUNCTIONS

/* makeNode takes the value to be put into a node
 * mallocs a node-size, assigns its data field
 * and assigns its pointer field to NULL
 */
Node* makeNode(int val) {
	Node* np = (Node*)malloc(sizeof(Node));
	if (np == NULL) return NULL;
	np->data = val;  
	np->next = NULL;
	return np;
}


/* headInsert takes value to be inserted and
 * a double pointer tothe first node in the list
 * it creates a list if top is NULL or 
 * creates a node and reassigns pointers
 * and returns 0 if successful and -1 if not
 */
int headInsert(int val, Node** top) {
	if (*top == NULL) *top = makeNode(val);
	Node* insert = makeNode(val);
	insert->next = *top;
	*top = insert;
	return 0;
}


/* tailInsert takes the value of the node to be created 
 * and a double pointer to top
 * it walks through the list and inserts the node at the end
 * it'll return the tail
 * and returns 0 if successful and -1 if not
 */
int tailInsert(int val, Node** top) {
	Node* np = makeNode(val);
	Node* curr = *top;
	if (curr == NULL) top = &np;
	while (curr->next != NULL) {
		curr = curr->next;
	}
	curr->next = np;
	return 0;
}


/* midInsert takes the value and position of the node to be created
 * and a double pointer to the top of the list to create it in
 * the function walks the list until it's at the correct position
 * then adds the node and reassigns pointers
 * and returns 0 if successful and -1 if not
*/
int midInsert(int val, int pos, Node** top) {
	int i;
	Node* curr = *top;
	if (curr == NULL || pos == 1) return headInsert(val, top);
	for (i = 1; i < pos-1; i++) {
		if (curr->next == NULL) return tailInsert(val, top);
		curr = curr->next;
	}
	Node* np = makeNode(val);
	np->next = curr->next;
	curr->next = np;
	return 0;
}



/* topDelete takes the pointer to the top pointer 
 * deletes the first node in the list
 * and returns the new top, or NULL
 * if the list is now empty
 * and returns 0 if successful and 1 if not
 */	
int topDelete(Node** top) {
	if (top == NULL) return 1;
	else {				//checks if the list is empty
		Node* temp = *top;
		top = temp->next;
		free(temp);
		return 0;
	}
}

/*mid delete--takes pointer to top pointer and position for parameters
 * walks through the list until it's before the node
 * to delete, then reassigns pointers and deletes
 * the relevant node
 * and returns 0 if successful and 1 if not
 */
int midDelete(int n, Node** top) {
	if (*top == NULL) return 1;
	Node* prev = *top;
	Node* curr = *top;
	if (n == 1) return topDelete(top);
	int i;
	for (i = 1; i < n; i++) {
		prev = curr;
		curr = curr->next;
	}
	prev->next = curr->next;
	free(curr);
	return 0;
}


/* delete by value, returning top of list
 * method: walk through the list until the 
 * value of the node beyond the one you're
 * on matches the value given.  Keep that 
 * node in a temp pointer, reassign pointers
 * and delete the node. 
 * and returns 0 if successful and -1 if not
*/
int deleteByVal(int val, Node** top) {
//make a variable to iterate with
	Node* curr = *top;
	Node* temp;
//check if it's the first node
	if (curr->data == val) return topDelete(top);
//for any node thereafter, get to the node
	while (curr->next->data != val) {
		if (curr == NULL) return 0; //if you get to the end of the list and value isn't there
	//	prev = curr;
		curr = curr->next;
	}
//you should be at the node;
//now you fix the links
	//	prev->next = curr->next;
	temp = curr->next;
	curr->next = curr->next->next;
//and free the node
	free(temp);
//and return the top
	return 0;
}



/* pop by value
 * walks through the list to find the value provided
 * assigns that value to a temp variable, reassigns
 * pointers, and frees the relevant node
 * then returns the integer.
*/
int popByValue(int val, Node** top) {		//takes the value you want to delete and the list pointer
	if (*top == NULL) return;					//don't play with empty lists
	Node* curr = *top;
	while (curr->next != NULL) {
		if (curr->next->data == val) {
			Node* np = curr->next;
			int temp = np->data;
			curr->next = curr->next->next;
			free(np);
			return temp;
		}
		curr = curr->next;
	}
	return;
}


/* print the list
 * takes top pointer (NOT double pointer)
 * walks through the list, printing every node
 * what's in it, where it is in memory
 * and where it's pointing to
*/
void printList(Node* top) {
	while (top != NULL) {
		printf("%d at %lx pointing to %lx\n", top->data, (unsigned long)top, (unsigned long)top->next);
		top = top->next;
	}
}




void main() {
	//initalize the top
	Node* top = makeNode(6);
	int status = headInsert(1222, &top);
	status = headInsert(32, &top);
	printList(top);

	printf("\ntailInsert:\n");
	status = tailInsert(87, &top);
	printList(top);

//mid delete
	printf("\npop by val: 1222\n");
	int val = popByValue(1222, &top);
	printf("val was %d\n", val);
										   //to insert at the top because you'd have to set top = midInsert
	printList(top);

	printf("\nmidInsert:\n");
	status = midInsert(773, 3, &top);  //it will handle a topInsert but you'll have to know that you're trying 
	status = midInsert(47, 2, &top);

	printList(top);

	printf("topDelete:\n");
	status = topDelete(&top);

	printList(top);
	printf("check!\n");

}