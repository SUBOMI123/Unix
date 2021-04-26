import sys
def Encoder(push):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    user_input = input("What is your message? ")
    check = ""
    output = ""
    result = ""
    for i in user_input:
        if i.lower() in alphabet:
            check +=i.upper()
    for j in check:
        if (ord(j) + push) > 90:
            output += chr(ord(j) - (26 - push))
        else:
            output += chr(ord(j) + push)
    counter = 5
    count = 0
    for a in range (0, len(output), 5):
        result += output[a:counter]
        result += " "
        counter += 5
        count += 1
        if (count % 10) == 0:
            result += "\n"
    return result

y = int(sys.argv[1])
print(Encoder(y))
