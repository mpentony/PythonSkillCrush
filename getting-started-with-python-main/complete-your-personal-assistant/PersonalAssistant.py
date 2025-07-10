class PersonalAssistant:
    def __init__(self, todos, birthdays, contacts):
        self.todos = todos
        self.birthdays = birthdays
        self.contacts = contacts

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
    
    def get_birthdays(self):
      return self.birthdays
    
    def get_contacts(self):
        return self.contacts

    def get_birthday(self, name):
      if name in self.birthdays:
          return f"{name}'s birthday is on {self.birthdays[name]}."
      else:
          return ("Birthday can not be found")
        
           
    def add_birthday(self, name, date):
       if name in self.birthdays:
          return f"{name}'s birthday is already on file."
       else:
          self.birthdays[name]=date
          return f"{name}'s birthday has been added."
        
    def remove_birthday(self, name):
       if name in self.birthdays:
           self.birthdays.pop(name)
           return f"{name}'s birthday has been removed from the file"
       else:
           return "Sorry, there is no recorded birthday for that person."
        
    def get_contact(self, name):
       if name in self.contacts:
          return f"{name} is a {self.contacts[name]}."
       else:
          return ("Sorry there is no contact by that name")
        
    def add_contact(self, name, position):
       if name in self.contacts:
           return f"You already have a contact by that name."
       else:
           self.contacts[name] = position
           return f"You have added {name}"
        
    def remove_contact(self, name):
       if name in self.contacts:
           self.contacts.pop(name)
           return f"{name} has been removed from the file"
       else:
           return "Sorry, there is no recorded contact."    