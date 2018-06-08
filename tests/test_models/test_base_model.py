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

    def test_base_model_save(self):
        """test the save method
        """
        self.bm1.save()
        self.assertNotEqual(self.bm1.created_at, self.bm1.updated_at)

    def test_base_model_to_dict(self):
        """test the to_dict method
        """
        bm1_dict = self.bm1.to_dict()
        self.assertIsInstance(bm1_dict['created_at'], str)
        self.assertIsInstance(bm1_dict['updated_at'], str)
        self.assertIsInstance(bm1_dict['id'], str)
        self.assertEqual(bm1_dict['__class__'], 'BaseModel')
        self.assertEqual(bm1_dict['my_number'], 89)
        self.assertEqual(bm1_dict['name'], 'Holberton')
