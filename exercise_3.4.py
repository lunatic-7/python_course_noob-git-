# num = input("any no. : ")
# total = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])
# print(f"the total of ur particular no. is {total}")
                                # OR  (BETTER METHOD)
number = input("enter a no. : ")
total = 0
i = 0
while i < len(number):
    total += int(number[i])
    i += 1
print(f"the total of ur particular no. is {total}")