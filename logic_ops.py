# logic_ops.py

def my_not(a):
    # Returns True if False, False if True without using the 'not' keyword
    if a == False:
        return True
    return False

def my_and(a, b):
    # Returns True only if both a and b are True without using the 'and' keyword
    if a == True:
        if b == True:
            return True
    return False

def my_or(a, b):
    # Returns False only if both a and b are False without using the 'or' keyword
    if a == False:
        if b == False:
            return False
    return True

def my_implies(a, b):
    # Truth table for implication (a implies b):
    # True -> True is True
    # True -> False is False
    # False -> True is True
    # False -> False is True
    if a == True:
        if b == False:
            return False
    return True

def evaluate(expr):
    # Base case: if expr is already a boolean (True or False)
    if isinstance(expr, bool):
        return expr

    # Extract operator name
    op = expr[0]

    # Handle unary operator: ("not", expr)
    if op == "not":
        sub_expr = expr[1]
        return my_not(evaluate(sub_expr))

    # Handle binary operators: ("and"|"or"|"implies", left, right)
    elif op == "and":
        left = expr[1]
        right = expr[2]
        return my_and(evaluate(left), evaluate(right))

    elif op == "or":
        left = expr[1]
        right = expr[2]
        return my_or(evaluate(left), evaluate(right))

    elif op == "implies":
        left = expr[1]
        right = expr[2]
        return my_implies(evaluate(left), evaluate(right))

    else:
        raise ValueError(f"Unknown operator: {op}")