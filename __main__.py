from abc import ABC, abstractmethod


class AbstractBot(ABC):
    @abstractmethod
    def handle(self, action):
        pass


class Book:
    def load(self, file_name):
        print(f"Loading contacts from {file_name}")

    def save(self, file_name):
        print(f"Saving contacts to {file_name}")


class Bot(AbstractBot):
    def __init__(self):
        self.book = Book()

    def handle(self, action):
        if action == 'add':
            print("Adding a contact...")
        elif action == 'remove':
            print("Removing a contact...")
        elif action == 'edit':
            print("Editing a contact...")
        else:
            print("Invalid command")


if __name__ == "__main__":
    print('Hello. I am your contact-assistant. What should I do with your contacts?')
    bot = Bot()
    bot.book.load("auto_save")
    commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']
    while True:
        action = input('Type help for a list of commands or enter your command:\n').strip().lower()
        if action == 'help':
            format_str = str('{:%s%d}' % ('^', 20))
            for command in commands:
                print(format_str.format(command))
            action = input().strip().lower()
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        else:
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        if action == 'exit':
            break
