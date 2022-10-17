#!/usr/bin/python3
"""files to json"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """HBNBCommand Class"""
    prompt = "(hbnb) "

    classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review}

    def do_create(self, arg):
        words = arg.split()
        if len(words) == 0:
            print("** class name missing **")
            return
        try:
            obj = HBNBCommand.classes[words[0]]()
            obj.save()
            print(obj.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, arg):
        words = arg.split()
        if len(words) < 1:
            print("** class name missing **")
        elif len(words) < 2:
            print("** instance id missing **")
        elif words[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            try:
                print(storage.all()[f"{words[0]}.{words[1]}"])
            except Exception:
                print("** no instance found **")

    def do_destroy(self, arg):
        words = arg.split()
        if len(words) < 1:
            print("** class name missing **")
        elif len(words) < 2:
            print("** instance id missing **")
        elif words[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            try:
                del storage.all()[f"{words[0]}.{words[1]}"]
                storage.save()
            except Exception:
                print("** no instance found **")

    def do_all(self, arg):
        words = arg.split()
        if words and words[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if words:
            objs = []
            for k, v in storage.all().items():
                if v.__class__.__name__ == words[0]:
                    objs.append(str(v))
            print(objs)
        else:
            print(storage.all())

    def do_update(self, arg):
        words = arg.split()
        if len(words) < 1:
            print("** class name missing **")
        elif len(words) < 2:
            print("** instance id missing **")
        elif words[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(words) < 3:
            print("** attribute name missing **")
        elif len(words) < 4:
            print("** value missing **")
        else:
            key = f"{words[0]}.{words[1]}"
            if not any(o[0] == key for o in storage.all().items()):
                print("** no instance found **")
                return
            setattr(storage.all()[key], words[2], words[3])

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        exit()

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
