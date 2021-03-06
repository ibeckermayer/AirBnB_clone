#!/usr/bin/python3
"""module for BaseModel
"""
import uuid
import datetime
import models


class BaseModel(object):
    """The base model that defines all common attributes/methods
       for other classes
    """

    def __init__(self, *args, **kwargs):
        """init method for BaseModel class

        Args:
            *args: not used
            **kwargs: dictionary of key word arguments
        """
        fmt = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, val in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.datetime.strptime(
                        kwargs['created_at'], fmt)
                elif key == "updated_at":
                    self.updated_at = datetime.datetime.strptime(
                        kwargs['updated_at'], fmt)
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """[<class name>] (<self.id>) <self.__dict__>

        Returns:
            str: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
           with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
           __dict__ of the instance

        Returns:
            dict: contains all keys/values of __dict__
                  of the instance with added key __class__
        """
        return_dict = self.__dict__.copy()
        return_dict['created_at'] = return_dict['created_at'].isoformat()
        return_dict['updated_at'] = return_dict['updated_at'].isoformat()
        return_dict['__class__'] = self.__class__.__name__
        return return_dict
