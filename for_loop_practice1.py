# cal. sum of  digits. ---> 1 + 2 + 3 ...
total = 0
num = input("enter a no. : ")
for i in range(0, len(num)):
    total += int(num[i])

print(f"the total of your particular no. is {total}")