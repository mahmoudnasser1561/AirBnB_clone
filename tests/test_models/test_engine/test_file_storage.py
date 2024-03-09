import os
import json
import models
import unitest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage_instantiation(unittest.TestCase):
	def test_fileStorage_instantaition_no_args(self):
		self.assertEqual(type(FileStorage()), FileStorage)
	def testFileStorage_instaniation_with_args(self):
		with self.assertRaises(TypeError):
			FileStorage(None)
	def test_FileStorage_file_path_is_private_str(self):
		self.assertEqual(str, type(FileStorage._FileStorage__file_path))
	def testFileStorage_objects_is_private_dict(self):
		self.assertEqual(dict, type(FileStorage.FileStorage__objects))
	def test_storage_initializes(self):
		self.assertEqual(type(models.storage), FileStorage)

