import datetime

current_time = datetime.datetime.now()

# print(current_time)

print(current_time.strftime("%m/%d/%y"))

print(current_time.strftime("%B %d, %Y"))

print(current_time.strftime("%B %d, %Y %I:%M %p"))