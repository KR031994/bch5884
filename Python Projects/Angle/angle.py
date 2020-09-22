#Python3 code to find all three angles of a triangle taking coordinates of all three vertices from user input
#Link to Repository Path:https://github.com/KR031994/bch5884.git
import math
Ax = float(input("Please enter the x coordinate of point A: ")) 
Ay = float(input("Please enter the y coordinate of point A: "))

Bx = float(input("Please enter the x coordinate of point B: ")) 
By = float(input("Please enter the y coordinate of point B: "))

Cx = float(input("Please enter the x coordinate of point C: ")) 
Cy = float(input("Please enter the y coordinate of point C: "))

d1 = Ax-Bx
d2 = Ay-By
d3 = Bx-Cx
d4 = By-Cy
d5 = Cx-Ax
d6 = Cy-Ay

AB2= (d1**2 + d2**2) # Square of length of side AB
BC2= (d3**2 + d4**2) # Square of length of side BC
CA2= (d5**2 + d6**2) # Square of length of side CA

AB = math.sqrt(d1**2 + d2**2) # Length of side AB
BC = math.sqrt(d3**2 + d4**2) # Length of side BC
CA = math.sqrt(d5**2 + d6**2) # Length of side CA

alpha = math.acos((BC2 + CA2 - AB2)/(2*BC*CA));
beta  = math.acos((AB2 + CA2 - BC2)/(2*AB*CA));
gamma = math.acos((AB2 + BC2 - CA2)/(2*AB*BC));

alpha = alpha*180/math.pi; # Measure of angle alpha in degree
beta  = beta*180/math.pi;  # Measure of angle beta in degree
gamma = gamma*180/math.pi; # Measure of angle gamma in degree

print("alpha : %f " % (alpha))
print("beta  : %f " % (beta))
print("gamma : %f " % (gamma))

