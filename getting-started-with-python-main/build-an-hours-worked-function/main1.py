# Write function here
def calculate_pay(hours_worked, pay_per_hour):
    pay = hours_worked * pay_per_hour
    return pay

# Worked 40 hours at $20 an hour
print(calculate_pay(40,20))

# Worked 50 hours at $20 an hour
print(calculate_pay(50,20))

# Worked 40 hours at $12 an hour
print(calculate_pay(40,12))
