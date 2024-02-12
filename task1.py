a = dict()
b = " "
c = " "
while b != "stop" or c != "stop" or b != "" or c != "":
    key = input()
    b = key
    if b == "stop" or b == "":
        break
    value = input()
    c = value
    if c == "stop" or c == "":
        break
    if b != "stop" or c != "stop" or b != "" or c != "":
        a[key] = value
print(a)