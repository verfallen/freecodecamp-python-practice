def separate_to_expression(problem):
    return problem.split(' ')


def arithmetic_arranger(problems, is_calculate=False):
    arranged_problems = []
    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''
    if len(problems) > 5:
        return 'Error: Too many problems.'

    for item in problems:
        expression = separate_to_expression(item)

        if expression[1] != '+' and expression[1] != '-':
            return "Error: Operator must be '+' or '-'."
        if not str.isdigit(expression[0]) or not str.isdigit(expression[2]):
            return 'Error: Numbers must only contain digits.'
        if len(expression[0]) > 4 or len(expression[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        len1 = len(expression[0])
        len2 = len(expression[2])

        # 每个算式的长度
        max_len = max(len1, len2) + 2

        expression[0] = expression[0].rjust(max_len)
        expression[2] = expression[2].rjust(max_len - 1)

        if is_calculate:
            if expression[1] == '+':
                expression.append(str(int(expression[0]) + int(expression[2])).rjust(max_len - 1))
            else:
                expression.append(str(int(expression[0]) - int(expression[2])).rjust(max_len - 1))
            fourth_line += expression[3].rjust(max_len) + '    '
        # print(expression)
        first_line += expression[0] + '    '
        second_line += expression[1] + expression[2] + '    '
        third_line += '-'.rjust(max_len, '-') + '    '

    # print(first_line)
    # print(second_line)
    # print(third_line)
    # print(fourth_line)

    # 删除多余的空格
    first_line = first_line[:-4]
    second_line = second_line[:-4]
    third_line = third_line[:-4]
    fourth_line = fourth_line[:-4]

    arranged_problems = first_line + '\n' + second_line + '\n' + third_line
    if is_calculate:
        arranged_problems += '\n' + fourth_line
    return arranged_problems
