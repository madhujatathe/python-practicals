r1 = int(input("Enter the value of r1"))
r2 = int(input("Enter the value of r2"))
r3 = int(input("Enter the value of r3"))
i1 = int(input("Enter the value of i1"))

a1 = (1/r1+1/r2)
b1 = (-1/r1)
c1 = i1

a2 = (-1/r1)
b2 = (1/r1+1/r3)
c2 = 0
# elimination method 
#multiply equation to eliminate v1
m1 = a2
m2 = a1

eq1_v2 = b1*m1
eq2_v2 = b2*m2

eq1_c = c1*m1
eq2_c = c2*m2

v2 = (eq2_c - eq1_c) / (eq2_v2 - eq1_v2)

v1 = (c1 - b1 * v2) / a1

print(v1)
print(v2)


