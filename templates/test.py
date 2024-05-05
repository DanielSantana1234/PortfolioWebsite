lst = []

def capitalize():
    while True:
        inp = input("Enter your sentence: ")
        if not inp:
            break
        lst.append(inp.upper())
        lst.append("\n")
    print(*lst)

capitalize()
