#!/usr/bin/python3
import cmd

# Define a list of valid class names
valid_classes = ["YourClass1", "YourClass2"]

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, line):
        if not line:
            print("**class name missing**")
            return 
        class_name = line.strip()
        if class_name not in valid_classes:
            print("**class doesn't exist**")
            return

        new_instance = classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def emptyline(self):
        """Do nothing"""
        pass

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
