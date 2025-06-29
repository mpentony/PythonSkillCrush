import json

show_data = []

with open("television_shows.txt", "r") as text_file:
  for line in text_file:
    show_data.append(line)

with open("top_shows.json", "w") as write_file:
  json.dump(show_data, write_file)