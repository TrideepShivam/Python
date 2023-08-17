str1 = input("please enter first string: ").lower()
str2 = input("please enter first string: ").lower()
found = False
for c in str1:
    if c in str2:
        pass
    else:
        found=True
        break
if found:
    print("not an anagram")
else:
    print("yes! anagram")