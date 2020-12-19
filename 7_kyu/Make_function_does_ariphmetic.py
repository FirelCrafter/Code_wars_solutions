def arithmetic(a, b, operator):
    return dict({"add": a + b, "subtract": a - b, "multiply": a * b, "divide": a / b})[operator]
