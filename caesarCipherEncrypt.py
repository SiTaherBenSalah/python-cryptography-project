def ci(ch):
    d = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
         "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    n = 3
    ch2 = ""
    for i in ch:
        if i == 'x' or i == "X":
            ch2 += 'A'
        elif i == 'Y' or i == "y":
            ch2 += 'B'
        elif i == 'Z' or i == "z":
            ch2 += 'C'
        else:
            for j in range(24):
                if d[j] == i or d[j].casefold() == i:
                    ch2 += d[j+n]
    return ch2
