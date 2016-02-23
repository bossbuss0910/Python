import random

def type(text):
    retest = []
    wordlist = [word for word in text.split(" ")]
    for w in wordlist:
        if len(w) > 4:
            retest.append(ram(w))
        else:
            retest.append(w)
    print " ".join(retest)

def ram(word):
    str = word[0]
    last = len(word)-1
    numlist = []
    count = 0
    while 1:
        num = random.randint(1,len(word)-2)
        if num not in numlist:
            numlist.append(num)
            str += word[num]
            count += 1
        if count == len(word)-2:
            break
    str += word[last]
    return str


type("Perfectly , I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")
