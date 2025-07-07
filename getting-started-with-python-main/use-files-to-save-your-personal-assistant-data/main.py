import json

#imports PersonalAssistant.py file
from PersonalAssistant import PersonalAssistant

#ADD CODE: open JSON file and pass data to PersonalAssistant class
todo_list = json.load(open("todo.json"))
assistant = PersonalAssistant(todo_list) #so old data shows in PersonalAssistant()


done = False

while not done:
    user_command = input(
        """
How can I help you?

    **** To-dos *****
    1: Add a to-do
    2: Remove a to-do
    3: Get to-do list

    Select a number or type 'Exit' to quit: 
    
    """
    )
    # Add Todo
    if user_command == "1":
        user_input = input("Item to add to to-do list: ")
        assistant.add_todo(user_input)
    # Remove Todo
    elif user_command == "2":
        print(f"Your current todos: {assistant.get_todos()}")
        user_input = input("Item to remove from to-do list: ")
        print(f"\n {assistant.remove_todo(user_input)}")
    # Get Todos
    elif user_command == "3":
        print("\nYour to-do list")
        print(f"\n {assistant.get_todos()}")
    elif user_command == "exit" or user_command == "Exit" or user_command == "EXIT":
        done = True
        print("\nGoodbye, see you soon!")
    else:
        print("\nNot a valid command.")

# ADD CODE: write data to JSON file
with open("todo.json", "w") as write_todos:
    json.dump(assistant.get_todos(), write_todos)
    print("To-do list saved!")
    print(f"\n {assistant.get_todos()}")
    print("\nGoodbye, see you soon!")
    done = True
    
     

    
