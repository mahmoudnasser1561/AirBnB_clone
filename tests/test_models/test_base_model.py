#!/usr/bin/python3

import unittest
from models.base_model import BaseModel

class TestBaseodel(unittest.TestCase):
        def test_init(self):
                my_model = BaseModel()
                self.assertIsNotNone(my_model.id)
                self.assertIsNotNone(my_model.created_at)
                self.assertIsNotNone(my_model.updated_at)

        def test_save(self):
                my_model = BaseModel()

                initial_updated_at = my_model.updated_at
                current_updated_at = my_model.save()
                self.assertNotEqual(initial_updated_at, current_updated_at)

        def test_to_dict(self):
                my_model = BaseModel()
                my_model_dictionary = my_model.to_dict()
                self.assertIsInstance(my_model_dictionary, dict)
                self.assertEqual(my_model_dictionary["__class__"], 'BaseModel')
                self.assertEqual(my_model_dictionary["id"], my_model.id)
                self.assertEqual(my_model_dictionary["created_at"], my_model.created_at.isoformat())
                self.assertEqual(my_model_dictionary["updated_at"], my_model.updated_at.isoformat())

        def test_str(self):
                my_model = BaseModel()
                self.assertTrue(str(my_model).startswith('[BaseModel]'))
                self.assertIn(my_model.id, str(my_model))
                self.assertIn(str(my_model.__dict__), str(my_model))
"""
	def test_to_dict(self):
		my_model = BaseModel()
		my_model_dict = my_model.to_dict()
		self.assertIsInstance(my_model_dict, dict)
		for key, value in my_model_dict.items():
			flag = 0
			if my_model_dict['__class__'] == 'BaseModel':
				flag += 1
			self.assertTrue(flag == 1)
		for key, value in my_model_dict.items():
			if key == 'created_at':
				self.assertIsInstance(value, str)
			if key == 'updated_at':
				self.assertIsInstance(value, str)
"""

if __name__ == "__main__" :
	unittest.main()                                                                                                                                                   
