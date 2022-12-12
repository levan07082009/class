sides=eval(input("enter the number of sides"))
a=eval(input("Enter the side: "))
import math as m
area=(sides * a ** 2)/ (4 * m.tan(m.pi/sides))
print("The area of the polygon is " + str(area))