class PersonalAssistant:
    def __init__(self, todos):

        self.todos = todos

    def get_contact(self, name):
      if name in self.contacts:
        return self.contacts[name]
      else:
        return "No contact with that name!"

    def add_todo(self, new_item):
      self.todos.append(new_item)

    def remove_todo(self, todo_item):
      # Checks if todo_item is in todos list
      if todo_item in self.todos:
        # Gets the todo_item index in list
        index = self.todos.index(todo_item)
        # pop the index for todo_item in todos list
        self.todos.pop(index)
        return f'{todo_item} was removed'
      else:
        print("To-do is not in list!")

    def get_todos(self):
      return self.todos

    def get_birthday(self, name):
      if name == "Mike":
          return "Birthday is 04/15/92!"
      elif name == "Jackie":
          return "Birthday is 07/12/98!"
      elif name == "Evelyn":
          return "Birthday is 02/31/85!"
      else:
          return "Can't find birthday for this person."

