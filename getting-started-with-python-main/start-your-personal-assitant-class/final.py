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

assistant=PersonalAssistant()
print(assistant.get_todos())
assistant.add_todo("Pick up toddler")
assistant.add_todo("Feed toddler")
assistant.add_todo("Give toddler a bath")
assistant.add_todo("Change diaper")
print(assistant.get_todos())
assistant.remove_todo("Feed toddler")
print(assistant.get_todos())
print(assistant.get_contact("Monique"))
print(assistant.get_birthday("Chelsea"))
      
