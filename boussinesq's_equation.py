#A concentrated load of 1000KN is appplied at the ground surface. write a program to compute the vertical pressure. 1)at adepthof 4m below the load. 2) at a distance of 3m at the same depth. use boussinesq's equation.
load = 1000 
r = 4
Z = 10
pi = 3.14159
Q = load / (pi * 0.5**2)


term_1  =3* Q/ 2 * pi * Z**2


sigma_z = term_1* (1/(1+(r/Z)**2))**5/2

print(f"Load (P) = {load} N")
print(f"Radius (r) = {r} m")
print(f"Depth (Z) = {Z} m")
print(f"Vertical stress (sigma_z) = {sigma_z:.4f} N/m^2")



