#1. wap to accept the cost price of a bike and display the road tax to be paid according to the following criteria
#costprice  tax
#100000     15%
#50k and <=100k     10%
#<=50000    5%
cp = int(input("cost prince of a bike:"))
tax=0
if cp<=50000:
    tax=5
elif cp>50000 and cp<=100000:
    tax=10
else:
    tax=15

print("your cost price :",cp)
print(tax,"% tax price :",cp*tax/100)
