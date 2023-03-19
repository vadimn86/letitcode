def valid(input_string: str):
    str_len = len(input_string)
    if str_len % 2:
        return False

    s = ''.join(sorted(input_string))
    print(s)
    for i in range(0, int(str_len / 2)):
        print(ord(s[i:i + 2][0]) - ord(s[i:i + 2][1]))
        if ord(s[i:i + 2][0]) - ord(s[i:i + 2][1]) not in (-1, -50, -2):
            return False

    return True


def valid_up(input_string: str):
    str_len = len(input_string)
    if str_len % 2:
        return False

    mapping = {"(": ")", "{": "}", "[": "]"}

    stack = []
    for index in range(0, str_len):
        if input_string[index] in mapping:
            stack.append(input_string[index])

        elif stack and input_string not in mapping:
            if mapping[stack[-1]] == input_string[index]:
                stack.pop()
            else:
                return False
        else:
            return False

    return not stack


if __name__ == "__main__":
    print(valid_up("))"))
    print(valid_up("([}}])"))
    print(valid_up("()[]{}"))
    print(valid_up("(]"))
    print(valid_up("([)]"))
    print(valid_up("({}[])"))
