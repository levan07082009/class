interger = eval(input("enter interger"))

p4 = interger % 10
p3 = (interger % 100) // 10
p2 = (interger // 100) % 10
p1 = interger // 1000



print(f"reversed number is {p4}{p3}{p2}{p1}")