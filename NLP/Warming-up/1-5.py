def wordn(text,n):
    listword = []
    nword = []
    sp = text.split(".")
    for i in range(len(sp)):
        list = sp[i].split(" ")
        for j in range(len(list)):
            listword.append(list[j])

    count = 0
    nlist = []
    str = ""
    for i in range(len(listword)):
       str += listword[i]
       count += 1
       if count == n:
           nlist.append(str)
           str = ""
           count = 0
       else:
           str += " "
    return nlist


def literaln(text,n):
    listword = []
    nword = []
    sp = text.split(".")
    for i in range(len(sp)):
        list = sp[i].split(" ")
        for j in range(len(list)):
            for l in range(len(list[j])):
                listword.append(list[j][l])

    count = 0
    nlist = []
    str = ""
    for i in range(len(listword)):
       str += listword[i]
       count += 1
       if count == n:
           nlist.append(str)
           str = ""
           count = 0
    return nlist

str = "I am a NLPer.You are good,perfectly."
nlist = wordn(str,2)
print nlist
nlist = literaln(str,2)
print nlist
