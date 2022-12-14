import math as m
cities = {
    "atlanta": (33.753874413304594, -84.40793795680763),
    "orlando": (28.544630839001975, -81.39175193589493),
    "savana": (32.090154279026386, -81.08756318078137),
    "charlotte": (35.23683665893397, -80.84715073782233),
}
x1, y1 = cities.get("atlanta")
x2, y2 = cities.get("orlando")
x3, y3 = cities.get("savana")
x4, y4 = cities.get("charlotte")

a=((x2 - x1)**2 + (y2 - y1)**2)**0.5
b=((x3 - x2)**2 + (y3 - y2)**2)**0.5
c=((x4 - x3)**2 + (y4 - y3)**2)**0.5
d=((x1 - x4)**2 + (y1 - y4)**2)**0.5

# pirveli samkutxedis fartobi

a1 = 1/2 * m.fabs(x1* y2 + x2 * y3 +x3 * y1- x1*y3 - x2 * y1 - y3 * y2)

a2 = 1/2 * m.fabs(x4* y2 + x2 * y3 +x3 * y4- x4*y3 - x2 * y4 - y3 * y2)


print("area of this surface is" + str(a1+a2))
