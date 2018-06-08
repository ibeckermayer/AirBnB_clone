"""module for BaseModel
"""
import uuid
import datetime


class BaseModel(object):
    """The base model that defines all common attributes/methods
       for other classes
    """

    def __init__(self):
        """init method for BaseModel class
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """[<class name>] (<self.id>) <self.__dict__>

        Returns:
            str: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, str(self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at
           with the current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
           __dict__ of the instance

        Returns:
            dict: contains all keys/values of __dict__
                  of the instance with added key __class__
        """
        return_dict = self.__dict__
        return_dict['created_at'] = return_dict['created_at'].isoformat()
        return_dict['updated_at'] = return_dict['updated_at'].isoformat()
        return_dict['__class__'] = self.__class__.__name__
        return return_dict
