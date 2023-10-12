#!/usr/bin/python3
import cmd

# Define a list of valid class names
valid_classes = ["BaseModel", "SomeOtherClass", "AnotherClass"]

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def do_create(self, line):
        if not line:
            return "**class name missing**"
        class_name = line.strip()
        if class_name not in valid_classes:
            return "**class doesn't exist**"
        def do_destroy(self,line):
            
         new_instance = BaseModel() 
         new_instance.save()  
         print(new_instance.id)  
    
    def emptyline(self):
         """Do nothing """
    pass
    
    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True
    
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
