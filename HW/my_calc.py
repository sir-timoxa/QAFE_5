def arithmetic(a, b, c):
    if c == "add":
        return a + b
    elif c == "subtract":
        return a - b
    elif c == "multiply":
        return a * b
    elif c=="divide":
        try:
            return a/b
        except ZeroDivisionError:
            print('Division by Zero')