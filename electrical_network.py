# program to solve electrical network(kcl) using python

# Example equations:
# (V1 - V2)/R1 + V1/R2 = I1
# (V2 - V1)/R1 + V2/R3 = 0

# Given values
R1 = 10
R2 = 5
R3 = 15
I1 = 2   # current entering node 1

# Convert equations into form:
# a1*V1 + b1*V2 = c1
# a2*V1 + b2*V2 = c2

a1 = (1/R1 + 1/R2)
b1 = (-1/R1)
c1 = I1

a2 = (-1/R1)
b2 = (1/R1 + 1/R3)
c2 = 0

# Solve using elimination method

V1 = (a2*c1 - a1*c2)/(a2*b1 - a1*b2)
V2 = (b1*c2 - b2*c1)/(a2*b1 - a1*b2)

print(f"Voltage at node 1 (V1) = {V1} V")
print(f"Voltage at node 2 (V2) = {V2} V")
