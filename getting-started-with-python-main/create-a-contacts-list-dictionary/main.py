people = ["Ann", "Chelsea", "Nichole", "Max"]
title = ["Marketing Coordinator", "Software Developer", "Sales Representative", "Technical Writer"]
#The key is person, the value is person_title
#Creating a dictionary


company_org = {}

for i in range(len(people)):
  person = people[i]
  person_title = title[i]
  key = person
  value = person_title
  company_org[person] = person_title
  
print(company_org)

company_org = {}

for i in range(len(people)):
  person = people[i]
  person_title = title[i]
  #key = person
  #value = person_title
  company_org[person] = person_title
  
print(company_org)