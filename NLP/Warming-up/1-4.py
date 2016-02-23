str = "Hi He Lied Because Boron Could Not Oxidize Fluorine.New Nations Might Also Sign Peace Security Clause. Arthur King Can."
list = str.split(".")
list2 = list[0].split(" ")
list3 = list[1].split(" ")
dic = {}
for i in range(len(list3)):
    list2.append(list3[i])
num = [1,5,6,7,8,9,15,16,19]
for i in range(len(list2)):
    if (i+1) in num:
        dic[i+1] = list2[i][0]
    else:
        dic[i+1] = list2[i][0] + list2[i][1]
print dic
