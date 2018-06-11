#!/usr/bin/python3
'''
Defines unittets for FileStorage class
'''
import unittest
import pep8
import os
import models.engine.file_storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorageClass(unittest.TestCase):
    '''Testing FileStorage Class
    '''
    test_json = "test_file.json"

    @classmethod
    def setUp(cls):
        """create class for each test
        """
        try:
            os.remove(TestFileStorageClass.test_json)
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__file_path = TestFileStorageClass.test_json
        FileStorage._FileStorage__objects = {}

    @classmethod
    def tearDown(cls):
        """create class for each test
        """
        try:
            os.remove(TestFileStorageClass.test_json)
        except FileNotFoundError:
            pass

    def test_file_storage_pep8(self):
        """test for pep8
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0,
                         'pep8 error in file_storage.py!')
        p = style.check_files(
            ['tests/test_models/test_engine/test_file_storage.py']
        )
        self.assertEqual(p.total_errors, 0,
                         'pep8 error in test_file_storage.py!')

    def test_base_model_docstrings(self):
        """test docstrings
        """
        self.assertIsNotNone(models.engine.file_storage.__doc__)
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_new(self):
        """test new()
        """
        bm1 = BaseModel()
        bm1.name = "Holberton"
        bm1.my_number = 89
        bm2 = BaseModel()
        bm2.name = "Holberton2"
        bm2.my_number = 90
        self.assertEqual(storage.all()[bm1.__class__.__name__ + '.' + bm1.id],
                         bm1)

        self.assertEqual(storage.all()[bm2.__class__.__name__ + '.' + bm2.id],
                         bm2)
        self.assertNotEqual(storage.all()[bm2.__class__.__name__
                                          + '.'
                                          + bm2.id], bm1)
        self.assertNotEqual(storage.all()[bm1.__class__.__name__
                                          + '.'
                                          + bm1.id], bm2)
        self.assertEqual(2, len(storage.all()))

    def test_save(self):
        """test save()
        """
        bm1 = BaseModel()
        bm1.name = "Holberton"
        bm1.my_number = 89
        bm2 = BaseModel()
        bm2.name = "Holberton"
        bm2.my_number = 89
        bm1.save()
        bm2.save()
        self.assertTrue(os.path.isfile(self.test_json))

    def test_save_no_objects(self):
        """test save with no objects
        """
        storage.save()
        self.assertFalse(os.path.isfile(self.test_json))

    def test_reload(self):
        """test reload()
        """
        bm1 = BaseModel()
        bm1.name = "Holberton"
        bm1.my_number = 89
        bm2 = BaseModel()
        bm2.name = "Holberton"
        bm2.my_number = 89
        bm1.save()
        bm2.save()
        FileStorage._FileStorage__objects = {}
        storage.reload()
        self.assertEqual(storage.all()[bm1.__class__.__name__
                                       + '.'
                                       + bm1.id].to_dict(),
                         bm1.to_dict())
        self.assertEqual(storage.all()[bm2.__class__.__name__
                                       + '.'
                                       + bm2.id].to_dict(),
                         bm2.to_dict())
        self.assertNotEqual(storage.all()[bm2.__class__.__name__
                                          + '.'
                                          + bm2.id].to_dict(),
                            bm1.to_dict())
        self.assertNotEqual(storage.all()[bm1.__class__.__name__
                                          + '.'
                                          + bm1.id].to_dict(),
                            bm2.to_dict())
        self.assertEqual(2, len(storage.all()))

    def test_reload_no_objects(self):
        """test reload with no objects
        """
        storage.reload()
        self.assertFalse(storage.all())
