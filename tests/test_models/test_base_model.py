#!/usr/bin/python3
'''
Defines unittets for BaseModel class
'''
import unittest
import pep8
import models.base_model
from models.base_model import BaseModel


class TestBaseModelClass(unittest.TestCase):
    '''Testing BaseModel Class
    '''

    @classmethod
    def setUpClass(cls):
        """create class for testing
        """
        cls.bm1 = BaseModel()
        cls.bm1.name = "Holberton"
        cls.bm1.my_number = 89

    @classmethod
    def tearDownClass(cls):
        """delete class after testing
        """
        del cls.bm1

    def test_base_model_pep8(self):
        """test for pep8
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0,
                         'pep8 error in models/base_model.py!')
        p = style.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(p.total_errors, 0,
                         'pep8 error in tests/test_models/test_base_model.py!')

    def test_base_model_docstrings(self):
        """test docstrings
        """
        self.assertIsNotNone(models.base_model.__doc__)
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_base_model_init(self):
        """test the init method
        """
        self.assertTrue(isinstance(self.bm1, BaseModel))
        self.assertEqual(self.bm1.created_at, self.bm1.updated_at)
        # bm1_dict = self.bm1.to_dict()
        # bm2 = BaseModel(bm1_dict)
        # print(bm1_dict)
        # print(bm2.to_dict())
        # self.assertEqual(self.bm1, bm2)
        # self.assertFalse(self.bm1 is bm2)

    def test_base_model_str(self):
        """test the __str__ implementation
        """
        self.assertEqual(str(self.bm1),
                         "[{}] ({}) {}".format(self.bm1.__class__.__name__,
                                               self.bm1.id,
                                               str(self.bm1.__dict__)))

    def test_base_model_save(self):
        """test the save method
        """
        self.bm1.save()
        self.assertNotEqual(self.bm1.created_at, self.bm1.updated_at)

    def test_base_model_to_dict(self):
        """test the to_dict method
        """
        bm1_dict = self.bm1.to_dict()
        self.assertIsInstance(bm1_dict, dict)
        self.assertIsInstance(bm1_dict['created_at'], str)
        self.assertEqual(bm1_dict['created_at'],
                         self.bm1.created_at.isoformat())
        self.assertIsInstance(bm1_dict['updated_at'], str)
        self.assertEqual(bm1_dict['updated_at'],
                         self.bm1.updated_at.isoformat())
        self.assertIsInstance(bm1_dict['id'], str)
        self.assertEqual(bm1_dict['id'], self.bm1.id)
        self.assertEqual(bm1_dict['__class__'], 'BaseModel')
        self.assertEqual(bm1_dict['my_number'], 89)
        self.assertEqual(bm1_dict['name'], 'Holberton')

    def test_base_model_init_kwargs(self):
        """test the init method with kwargs
        """
        bm1_dict = self.bm1.to_dict()
        bm2 = BaseModel(**bm1_dict)
        self.assertFalse(self.bm1 is bm2)
        self.assertNotEqual(self.bm1, bm2)
        self.assertEqual(self.bm1.id, bm2.id)
        self.assertEqual(self.bm1.created_at, bm2.created_at)
        self.assertEqual(self.bm1.updated_at, bm2.updated_at)
        self.assertEqual(self.bm1.my_number, bm2.my_number)
        self.assertEqual(self.bm1.name, bm2.name)
