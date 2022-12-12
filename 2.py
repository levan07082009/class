point1 = eval(input("Enter point 1 (latitude and longitude) in degrees:"))
point2 = eval(input("Enter point 2 (latitude and longitude) in degrees:"))
import math as m

radius = 6371.01
x1, y1 = point1
x1=m.radians(x1)
y1=m.radians(y1)

x2, y2 = point2
x2=m.radians(x2)
y2=m.radians(y2)
d = radius * m.acos(m.sin ( x1 ) * m.sin ( x2 ) + m.cos( x1 ) * m.cos( x2 ) * m.cos( y1 - y2 ))
print("The distance between the two points is " + d)