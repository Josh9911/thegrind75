def isValid(s: str) -> bool:
    stack = []

    element_dict = {
            """(""" : """)""",
            """{""" : """}""",
            """[""" : """]"""
            }
    
    for element in s:
        if element in element_dict.keys():
            stack.append(element)
        elif element not in element_dict.keys() and element_dict[stack.pop()] == element:
            stack.pop()
        else:
            return False

    return len(stack) == 0


print(isValid(s="()"))

print(isValid("()[]{}"))

print(isValid("(]"))

print(isValid("([)]"))

