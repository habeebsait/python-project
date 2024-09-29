def evaluate_expression(expression):
    """Evaluates a given arithmetic expression.

    Args:
        expression: The arithmetic expression to evaluate.

    Returns:
        The result of the evaluation.
    """

    nums = []
    ops = []
    num = ""

    for char in expression:
        if char.isdigit():
            num += char
        else:
            if num:
                nums.append(float(num))
            num = ""
            ops.append(char)

    if num:
        nums.append(float(num))

    result = nums[0]

    def evaluate_operation(result, num2, op):
        if op == "*":
            return result * num2
        elif op == "/":
            if num2 == 0:
                raise ValueError("Division by zero is not allowed.")
            return result / num2
        elif op == "+":
            return result + num2
        elif op == "-":
            return result - num2
        else:
            raise ValueError("Invalid operator: " + op)

    for i in range(len(ops)):
        if ops[i] == "*" or ops[i] == "/":
            result = evaluate_operation(result, nums[i + 1], ops[i])
        else:
            result += nums[i + 1] if ops[i] == "+" else -nums[i + 1]

    return result

expression = input("Enter your arithmetic expression: ")
result = evaluate_expression(expression)
print("Result:", result)