todo_list = []
done = False

print("Type 'done' at any time to exit")

while not done:
  new_item = input("Add an item to todo list: ")

  if new_item == "done":
    done = True
  else:
    todo_list.append(new_item)

print(todo_list)
