def valid_parenthesis(s):
    brackets = []
    opening_bracket = {'}': '{', ')': '(', ']': '['}
    for bracket in s:
        if bracket in "}])":
            if len(brackets) == 0:
                return False
            if opening_bracket[bracket] != brackets.pop():
                return False
        else:
            brackets.append(bracket)
    if brackets:
        return False
    else:
        return True
