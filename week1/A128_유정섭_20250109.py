# https://www.acmicpc.net/problem/4949

while True:
    s = input()
    if s == ".":
        break
    stack = []
    result = True
    for c in s:
        if c == "(":
           stack.append("(") 
        elif c == "[":
            stack.append("[")
        elif c == ")" and (len(stack) == 0 or stack.pop() != "("):
            result = False
            break
        elif c == "]" and (len(stack) == 0 or stack.pop() != "["):
            result = False
            break
    print("yes" if result and len(stack) == 0 else "no")

        