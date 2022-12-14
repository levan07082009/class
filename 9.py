name = input("Enter employee's name: ")
hours = eval(input("Enter number of hours worked in a week (e.g., 10): "))
pay_rate = eval(input("Enter hourly pay rate (e.g., 9.75):"))
tax = eval(input("Enter federal tax withholding rate (e.g., 20%): "))
rate = eval(input("Enter state tax withholding rate (e.g., 9%): "))





print(f"Employee Name: {name}")
print(f"Hours Worked: {hours}")
print(f"Pay Rate: {pay_rate}")
print(f"Gross Pay:{pay_rate * hours}")
print("Deductions:")
print(f"   Federal Withholding ({tax*100}%): {hours * tax*pay_rate:.3}")
print(f"   State Withholding ({tax*100}%): {hours * rate*pay_rate:.3}")
print(f"   Total Deduction: {hours * tax*pay_rate + rate* hours *pay_rate:.4} Net Pay: {hours*pay_rate - (hours * tax*pay_rate + rate* hours *pay_rate):.4}")
