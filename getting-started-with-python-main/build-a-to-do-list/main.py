todo_list = []
done = False

print("Type 'done' at any time to exit")

while not done:
    task = input("Enter a task: ")
  
    if task == "done":
        done = True  # Exit loop
    else: 
        todo_list.append(task)
print(todo_list)   
            