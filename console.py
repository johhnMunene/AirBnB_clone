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

    def precmd(self, line):
        line = line.strip()
        self._step.set_last_user_input(line)
        if self._step.block_command(line):
            self._set_command_blocked(True)
            return cmd.Cmd.precmd(self, "return to default")
        else:
            self._set_command_blocked(False)
            return cmd.Cmd.precmd(self, line)

def create_too_many_wrong_args(self):
        """Tests create with too many args all incorrect"""
        pass

    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
