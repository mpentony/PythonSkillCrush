age_list = [5,7,12,13,9,8,11,10]
num_eligible = 0

for value in age_list:
    if value > 9:
        num_eligible = num_eligible + 1

print(num_eligible)
