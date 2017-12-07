# Given a stack of N elements, interleave the first half of the stack with the second half reversed using one other queue. 
# For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3].

from collections import deque

# Purpose: 
# Reach a state like this: stack: [4,5], queue: [1,2,3], then interleave by popping stack and queue alternatively then push to stack
# first move all to queue --> stack: [], queue: [5,4,3,2,1]
# split --> stack: [5,4], queue: [3,2,1]
# exchange --> stack: [3,2,1], queue: [4,5]
# exchange again --> stack: [4,5], queue: [1,2,3]
# interleave --> stack: [], queue: [1,5,2,4,3]
# stack get it all: stack: [1,5,2,4,3] , queue: []

def swap(stack, queue):
	queue_length = len(queue)
	while (stack):
		queue.append(stack.pop())
	for i in range(queue_length):
		stack.append(queue.popleft())


def interleave(stack):
	queue = deque([])
	half_length = len(stack)//2

	# empty stack to queue
	swap(stack, queue)

	for i in range(half_length):
		stack.append(queue.popleft())

	difference = len(queue) - half_length

	swap(stack, queue)

	swap(stack, queue)

	# interleave
	while (stack):
		queue.append(queue.popleft())
		queue.append(stack.pop())

	for i in range(difference):
		queue.append(queue.popleft())

	while (queue):
		stack.append(queue.popleft())
	
	return stack


_input1 = [1,2,3,4,5]
_output1 = [1,5,2,4,3]

_input2 = [i for i in range(11,21)]
_output2 = [11,20,12,19,13,18,14,17,15,16]

# print(interleave(_input))

assert interleave(_input1) == _output1, 'Wrong'
assert interleave(_input2) == _output2, 'Wrong'
