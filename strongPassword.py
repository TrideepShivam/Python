userInput = input("Please Enter Your Password :")
print("password : ",userInput)

spec = "`~!@#$%^&*()_+-={[]}\|/?><,."

havingAlNum = False
havingUpper = False
havingSpec = False
#check that str contains illegal character or not
for c in userInput:
    if c.isnumeric() and havingAlNum==False:
        havingAlNum=True
    if c.isupper() and havingUpper==False:
        havingUpper=True
    if c in spec and havingSpec==False:
        havingSpec=True
#print pass is 
if havingAlNum:
    print("Alphanumeric Passed.")
else:
    print("Alphanumeric Failed")

if havingUpper:
    print("Uppercase passed")
else:
    print("Uppercase Failed")

if havingSpec:
    print("Special Character Passed")
else:
    print("Special Character Failed")