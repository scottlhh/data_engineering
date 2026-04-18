"""
https://leetcode.com/problems/valid-parentheses/description/
"""
def is_valid_parenthses(intput_str: str):
    p_stack = []
    p_pair = {")": "(", "]": "[", "}": "{"}
    for p in list(intput_str):
        prev_p = p_stack[-1] if len(p_stack) > 0 else None
        if prev_p is not None and prev_p == p_pair.get(p):
            if len(p_stack) > 0:
                p_stack.pop()
            else:
                return False
        elif p is not None:
            p_stack.append(p)
    return len(p_stack) == 0


input1 = "()"
input2 = "()[]{}"
input3 = "(]"
input4 = "([])"
input5 = "([)]"
input6 = "()])"

inputs = [input1]
inputs = [input1, input2, input3, input4, input5, input6]

if __name__ == "__main__":
    for i in inputs:
        is_valid = is_valid_parenthses(i)
        print(f'Input :"{i}" is_valid:{is_valid}')
        print('this is good')

