class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.data

def precedence(operator):
    if operator in ('+', '-'):
        return 1
    if operator in ('*', '/'):
        return 2
    if operator == '^':
        return 3
    return 0

def is_operator(char):
    return char in ('+', '-', '*', '/', '^')

def is_operand(char):
    return char.isalnum()

def infix_to_postfix(expression):
    stack = LinkedListStack()
    postfix = []
    steps = []

    for char in expression:
        if char == ' ':
            continue
        if is_operand(char):
            postfix.append(char)
            steps.append(''.join(postfix))
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
                steps.append(''.join(postfix))
            if not stack.is_empty() and stack.peek() == '(':
                stack.pop()
        elif is_operator(char):
            while (not stack.is_empty() and
                   precedence(char) <= precedence(stack.peek())):
                postfix.append(stack.pop())
                steps.append(''.join(postfix))
            stack.push(char)

    while not stack.is_empty():
        postfix.append(stack.pop())
        steps.append(''.join(postfix))

    return ''.join(postfix), steps
