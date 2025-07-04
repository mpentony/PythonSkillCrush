people = ["Ann", "Chelsea", "Nichole", "Max"]
title = ["Marketing Coordinator", "Software Developer", "Sales Representative", "Technical Writer"]

company_org = {}

for i in range(len(people)):
  person = people[i]
  person_title = title[i]
  key = person
  value = person_title
  print(key + " is the " + value)
  