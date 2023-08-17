str1 = input("please enter first string: ").lower()
found = False
for x in range(len(str1)//2):
    if str1[x]==str1[-1-x]:
        pass
    else:
        found=True
        break
if found:
    print("not pelindrom")
else:
    print("yes! pelindrom")