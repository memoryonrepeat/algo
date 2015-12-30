/*
PROBLEM DESCRIPTION:

Given a deck containing n cards.  While holding the deck:

    Take the top card off the deck and set it on the table.
    Take the next card off the top and put it on the bottom of the deck in your hand.
    Continue steps 1 and 2 until all cards are on the table.  This is a round.
    Pick up the deck from the table and repeat steps 1-3 until the deck is in the original order.

Write a program to determine how many rounds it will take to put a deck back into the original order.  This will involve creating a data structure to represent the order of the cards. This program should be written in C, C++, Java or JavaScript/Node.js, and should be executable from the command line. It should take a number of cards in the deck as a command line argument and write the result to stdout.
For a JavaScript solution, do not use any Array methods.
*/

/*
SOLUTION:

The operations on the hand are similar to queue's enqueue and dequeue
The operations on the table are similar to stack's push and pop

Therefore, the idea is to simulate the shuffling process by
using a queue for the hand and a stack for the table.

Since JavaScript array is not allowed, i implemented the stack and queue 
using a linked-list approach from scratch. 

Cards are represented as positive values starting at 1, constantly increasing by 1
E.g: 1 2 3 4 5 6 7 8 9 10 ...

The shuffling will stop once the queue (which simulates the hand) are in the original order

A test file shuffle_test.txt is also provided, which contains test cases from 1 to 50

To test: 
node shuffle.js shuffle_test.txt
*/

var fs  = require("fs");

//Node is the fundamental unit inside stack/queue
var Node = function(value){
    this.value = value;
    this.next = null;
}

Node.prototype.hasNext = function(){
	return this.next != null;
}

var Stack = function(){
	this.top=null;
}

Stack.prototype.isEmpty = function(){
	return this.top == null;
}

Stack.prototype.push = function(value){
	var new_node = new Node(value);
	if (this.isEmpty()){
		this.top = new_node;
	}
	else{
		new_node.next = this.top;
		this.top = new_node;
	}
}

Stack.prototype.pop = function(){
	if (this.isEmpty()) return null;
	var value = this.top;
	this.top = this.top.next;
	return value;	
}

Stack.prototype.print = function(){
	if (this.isEmpty()) return;
	var current = this.top;
	while (current!=null){
		console.log(current.value);
		current = current.next;
	}
}

var Queue = function(){
	this.first = null;
}

Queue.prototype.isEmpty = function(){
	return this.first == null;
}

Queue.prototype.enqueue = function(value){
	var new_node = new Node(value);
	if (this.isEmpty()){
		this.first = new_node;
	}
	else{
		current = this.first;
		while(current.hasNext()){
			current = current.next;
		}
		current.next = new_node;
	}
}

Queue.prototype.dequeue = function(){
	if (this.isEmpty()) return null;
	var value = this.first;
	this.first = this.first.next;
	return value;
}

Queue.prototype.print = function(){
	if (this.isEmpty()) return;
	current = this.first;
	while (current!=null){
		console.log(current.value);
		current = current.next;
	}
}

Queue.prototype.peek = function(){
	if (this.isEmpty()) return null;
	return this.first;
}

/*
Check if elements in queue are already shuffled to the cards' order
*/
Queue.prototype.isInOrder = function(){ 
	if (this.isEmpty()) return true;
	current = this.peek();
	while (current.hasNext()){
		if (current.next.value-current.value!=1) return false;
		current = current.next;
	}
	return true;
}

/*
Simulate the shuffling process
Table is stack
Hand is queue
*/
function shuffle(hand,table){

	while (!hand.isEmpty()){ //Hand has at least one card
		var top_card = hand.dequeue();		
		table.push(top_card.value); //Top card to the table		
		if (!hand.isEmpty()){ //Hand has at least two cards
			var second_card = hand.dequeue();									
			hand.enqueue(second_card.value); //Next-to-top card to the bottom of the hand
		}
	}

	/*
	After all cards are all table -> put them back to hand
	*/
	while(!table.isEmpty()){ 
		current_card = table.pop();
		hand.enqueue(current_card.value);
	}
}

function count_shuffle(total_cards){
	var table = new Stack();
	var hand = new Queue();

	var count = 0;

	/*
	Cards are represented as positive numbers, starting from 1, constantly increase by 1
	E.g: 1 2 3 4 5 6 7 8 9 10 ...
	*/
	for (var i=1; i<=total_cards; i++){
		hand.enqueue(i);
	}		

	/*
	Keep shuffling until the cards are in the original order
	*/
	while(!hand.isInOrder() || count==0){		
		shuffle(hand,table);
		count++;
	}
	return count;
}

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
	if (line === "") return;

	var args = line.split(' ').map(function(n) { return parseInt(n, 10); });

	var total_cards = args[0];
	
	var result = count_shuffle(total_cards);		
	to_write = 'Need '+result+' rounds to shuffle '+total_cards+' cards to the original order\n';

	process.stdout.write(to_write);
});






