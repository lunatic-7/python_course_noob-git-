# to count no. of char. in ur name using for loop
name = input("enter ur name : ")
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]} : {name.count(name[i])}")
        temp += name[i]