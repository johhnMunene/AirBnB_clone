#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.User import User
from models.amenity import Amenity
from models.City import City
from models.Place import Place
from models import storage

# Define a list of valid class names
valid_classes = ["BaseModel", "User", "State",
                     "City", "Amenity", "Place", "Review"]

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

def create_too_many_wrong_args(self):
        """Tests create with too many args all incorrect"""
        pass

    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
