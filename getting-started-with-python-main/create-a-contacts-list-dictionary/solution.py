people = ["Ann", "Chelsea", "Nichole", "Max"]
title = ["Marketing Coordinator", "Software Developer", "Sales Representative", "Technical Writer"]

company_org = {}

for i in range(len(people)):
    person = people[i]
    person_title = title[i]
    company_org[person] = person_title

print(company_org)