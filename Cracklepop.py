for i in range(1,101):
    out = ""
    if i % 3 == 0:
        out += "Crackle"
    if i % 5 == 0:
        out += "Pop"
    if not out:
        out = i
    print(out)