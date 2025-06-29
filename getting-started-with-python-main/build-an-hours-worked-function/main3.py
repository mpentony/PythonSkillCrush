# Write function here
def calculate_monthly_pay(wk_1_hours, wk_2_hours, wk_3_hours, wk_4_hours, pay_per_hour):
    weekly1_pay = calculate_pay(wk_1_hours, pay_per_hour)
    weekly2_pay = calculate_pay(wk_2_hours, pay_per_hour)
    weekly3_pay = calculate_pay(wk_3_hours, pay_per_hour)
    weekly4_pay = calculate_pay(wk_4_hours, pay_per_hour)
    monthly_pay = weekly1_pay + weekly2_pay + weekly3_pay + weekly4_pay
    return monthly_pay


def calculate_pay(hours_worked, pay_per_hour):
    if hours_worked >40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_per_hour * 2) 
        regular_pay = 40 * pay_per_hour 
        pay = regular_pay + overtime_pay
    else:   
        pay = hours_worked * pay_per_hour
    return pay

# Worked 40 hours at $20 an hours,worked 50 hours at $20, worked 40 hours at $12 hour
print(calculate_monthly_pay(40,50,40,0,20))
