#!/usr/bin/python3
"""console module"""
import cmd
from models.base_model import BaseModel
import models
import shlex


class HBNBCommand(cmd.Cmd):
    """command interpreter class for HBNB"""
    available_models = ["BaseModel"]
    prompt = '(hbnb) '
    storage = models.storage

    def emptyline(self):
        """make it so emptyline executes nothing
        """
        pass

    def do_EOF(self, line):
        """Quit command to exit the program
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_create(self, model):
        """Creates a new instance of model, saves it and prints the id
        """
        if not model:
            print("** class name missing **")
        elif model not in self.available_models:
            print("** class doesn't exist **")
        else:
            if model == "BaseModel":
                bm = BaseModel()
                bm.save()
                print(bm.id)

    def do_show(self, model_and_id):
        """Prints the string of an instance based on the class name and id
        """
        model_and_id_list = model_and_id.split()
        if len(model_and_id_list) == 0:
            print("** class name missing **")
            return
        else:
            model = model_and_id_list[0]
            if model not in self.available_models:
                print("** class doesn't exist **")
                return
        if len(model_and_id_list) == 1:
            print("** instance id missing **")
            return
        else:
            idd = model_and_id_list[1]
            try:
                print(self.storage.all()[model + "." + idd])
                return
            except KeyError:
                print("** no instance found **")
                return

    def do_destroy(self, model_and_id):
        """destroys an instance based on the class name and id
        """
        model_and_id_list = model_and_id.split()
        if len(model_and_id_list) == 0:
            print("** class name missing **")
            return
        else:
            model = model_and_id_list[0]
            if model not in self.available_models:
                print("** class doesn't exist **")
                return
        if len(model_and_id_list) == 1:
            print("** instance id missing **")
            return
        else:
            idd = model_and_id_list[1]
            try:
                del self.storage.all()[model + "." + idd]
                self.storage.save()
                return
            except KeyError:
                print("** no instance found **")
                return

    def do_all(self, model):
        if not model:
            for key, obj in self.storage.all().items():
                print(obj)
        elif model not in self.available_models:
            print("** class doesn't exist **")
        else:
            for key, obj in self.storage.all().items():
                if obj.__class__.__name__ == model:
                    print(obj)

    def do_update(self, model_id_attr_val):
        model_id_attr_val_list = shlex.split(model_id_attr_val)
        if len(model_id_attr_val_list) == 0:
            print("** class name missing **")
            return
        else:
            model = model_id_attr_val_list[0]
            if model not in self.available_models:
                print("** class doesn't exist **")
                return

        if len(model_id_attr_val_list) == 1:
            print("** instance id missing **")
            return
        else:
            idd = model_id_attr_val_list[1]
            try:
                obj = self.storage.all()[model + "." + idd]
            except KeyError:
                print("** no instance found **")
                return

        if len(model_id_attr_val_list) == 2:
            print("** attribute name missing **")
            return
        else:
            attr = model_id_attr_val_list[2]

        if len(model_id_attr_val_list) == 3:
            print("** value missing **")
            return
        else:
            val = model_id_attr_val_list[3]

        setattr(obj, attr, cast_int_float_or_str(val))
        obj.save()


def cast_int_float_or_str(val):
    """cast the value to its proper type

    Args:
       val (str): the value being cast

    Returns:
        int, float, or str: proper type depending on val
    """
    try:
        return int(val)
    except ValueError:
        pass
    try:
        return float(val)
    except ValueError:
        return val


if __name__ == '__main__':
    HBNBCommand().cmdloop()
