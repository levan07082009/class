name = input("Enter employee's name: ")
hours = input("Enter number of hours worked in a week (e.g., 10): ")
pay_rate = input("Enter hourly pay rate (e.g., 9.75):")
tax = input("Enter federal tax withholding rate (e.g., 20%): ")
rate = input("Enter state tax withholding rate (e.g., 9%): ")





print(f"Employee Name: {name}")
print(f"Hours Worked: {hours}")
print(f"Pay Rate: {pay_rate}")
print(f"Gross Pay:{int(pay_rate) * int(hours)}")

