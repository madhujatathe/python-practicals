unit = float(input("enter the unit: "))
bill =0
fixed =50
if unit <=100:
    bill =unit*1.5
elif unit<=200:
    bill =(100*1.5)+(unit-100)*2
elif unit<=300:
    bill = (100*1.5)+(100*2)+(unit-100)*2.5
else:
    bill =(100*1.5)+(100*2)+(100*2.5)+(unit-100)*4


total = bill+fixed
print("the total bill is :",total)
