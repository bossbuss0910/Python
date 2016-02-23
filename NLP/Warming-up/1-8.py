def cipher(text):
    str = ""
    for i in text:
        if i.islower():
            str += chr(219-ord(i))
        else:
            str += i
    print str

cipher("sentAA11ence")
