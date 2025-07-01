import datetime

current_time = datetime.datetime.now()
print("Current Time = ", current_time)

print()

mdydate=current_time.strftime("%m/%d/%y")
print("Current Time in Month, Day and Year =", mdydate)

mdy=current_time.strftime("%B %d, %Y")
print("Current Time in Month, Day and Year =", mdy)

mdytime = current_time.strftime("%B %d, %Y %I:%M %p")
print("Current Time in Month, Day and Year =", mdytime)
