def arithmetic_arranger(problems, show_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize variables
    arranged_problems = []
    line1 = ""
    line2 = ""
    dashes = ""
    results = ""

    # Loop through each problem
    for problem in problems:

        # Split problem into operands and operator
        operands = problem.split()
        num1 = operands[0]
        operator = operands[1]
        num2 = operands[2]

        # Check if operator is valid
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Check if operands contain digits only
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        # Check if operands have max of four digits
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine length of longest operand for spacing
        max_length = max(len(num1), len(num2))

        # Create top line of problem
        line1 += num1.rjust(max_length + 2)
        line1 += "    "

        # Create bottom line of problem
        line2 += operator + " " + num2.rjust(max_length)
        line2 += "    "

        # Create dashes line of problem
        dashes += "-" * (max_length + 2)
        dashes += "    "

        # Calculate result if flag is True
        if show_answers:
            if operator == "+":
                result = str(int(num1) + int(num2))
            else:

                result = str(int(num1) - int(num2))

            results += result.rjust(max_length + 2)
            results += "    "

    # Append lines to arranged_problems list
    arranged_problems.append(line1.rstrip())
    arranged_problems.append(line2.rstrip())
    arranged_problems.append(dashes.rstrip())

    # Append results if flag is True
    if show_answers:
        arranged_problems.append(results.rstrip())

    # Return arranged problems as a string
    return "\n".join(arranged_problems)

x = arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])
print(x)