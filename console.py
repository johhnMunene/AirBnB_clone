#!/usr/bin/python3
import cmd


class HBNBcommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def emptyline(self):
         """Do nothing """
    pass
    def do_EOF(self,line):
        """EOF command to exit the program"""
        return True
    def do_quit(self,line):
        """Quit command to exit the program"""
        return True
    
    
    
if __name__ == '__main__':
        HBNBcommand().cmdloop()