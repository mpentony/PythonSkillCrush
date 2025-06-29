# Give the class a name
class PersonalAssistant:
    # Add an __init__ function here
    def __init__(self, todos, birthdays, contacts):
        self.todos = todos
        self.birthdays = birthdays
        self.contacts = contacts

    def add_todo(self, new_item):
        self.todos.append(new_item)
        return f"{new_item} has been added to your todo list"

    def remove_todo(self, new_item):
        if new_item in self.todos:
            self.todos.remove(new_item)
            return f"{new_item} removed from todo list."
        else:
            return f"To-do is not in list!"

    def get_todos(self):
        return self.todos

    def get_birthday(self, name):
        if name in self.birthdays:
            return f"{name}'s birthday is on {self.birthdays[name]}."
        else:
            return "Can't find birthday for this person."

    def get_birthdays(self):
        return self.birthdays

    def add_birthday(self, name, date):
        if name in self.birthdays:
            return f"You already have a birthday for {name}"
        else:
            self.birthdays[name] = date
            return f"{name}'s birthday has been added."

    def remove_birthday(self, name):
        if name in self.birthdays:
            self.birthdays.pop(name)
            return f"{name}'s birthday has been removed."
        else:
            return "Sorry, there is no recorded birthday for that person."

    def get_contact(self, name):
        if name in self.contacts:
            return f"{name} is a {self.contacts[name]}"
        else:
            return "Sorry, there is no contact by that name."

    def add_contact(self, name, position):
        if name in self.contacts:
            return f"You already have a contact by that name."
        else:
            self.contacts[name] = position
            return f"You have added {name}"

    def remove_contact(self, name):
        if name in self.contacts:
            self.contacts.pop(name)
            return f"{name} has been removed."
        else:
            return f"{name} is not in your contacts, could not remove."

    def get_contacts(self):
        return self.contacts
