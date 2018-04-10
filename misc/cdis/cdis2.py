def is_balanced(parens):
    stack = []
    for paren in parens:
        if paren=="(":
            stack.append(paren)
        else:
            if len(stack)==0:
                return False
            else:
                stack.pop()
    if len(stack)>0:
        return False
    return True
    

assert is_balanced("()()()()")==True, is_balanced("()()()()")
assert is_balanced(")()()()(")==False, is_balanced(")()()()(")
assert is_balanced("((())())")==True, is_balanced("((())())")
assert is_balanced("(((((())")==False, is_balanced("(((((())")
assert is_balanced("(()))))")==False, is_balanced("(()))))")
assert is_balanced("")==True, is_balanced("")
assert is_balanced("(")==False, is_balanced("(")
assert is_balanced(")")==False, is_balanced(")")