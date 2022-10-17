#!/usr/bin/python3
"""HBNBComand Module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand Class"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        exit()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
