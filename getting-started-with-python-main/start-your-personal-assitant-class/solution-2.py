class PersonalAssistant:

  def __init__(self):
    self.contacts = {
        'Ann': 'Marketing Coordinator', 'Chelsea': 'Software Developer','Nichole': 'Sales Representative'
    }
    self.todos = []


  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
      # Get the todo_item index in list
      index = self.todos.index(todo_item)
      # pop the index for todo_item in todos list
      self.todos.pop(index)
    else:
      print("Todo is not in list!")
      
  def get_todos(self):
    return self.todos

  def get_birthday(self, name):
    if name == "Ann":
      return "Birthday is 10/12/1991!"
    elif name == "Chelsea":
      return "Birthday is 12/23/1992!"
    elif name == "Nichole":
      return "Birthday is 01/01/1993!"
    else:
      return "Can't find a birthday for this person..."
      
  def get_contact(self, name):
    if name in self.contacts:
        return self.contacts[name]
    else:
        return "No contact with that name!"


# Code to test the class
assistant = PersonalAssistant()
assistant.add_todo("Pick up groceries")
assistant.add_todo("Schedule meeting for next week")
print(assistant.get_todos())
assistant.remove_todo("Pick up groceries")
print(assistant.get_todos())
# Change names to use your own data
print(assistant.get_contact("Chelsea"))
print(assistant.get_birthday("Ann"))
