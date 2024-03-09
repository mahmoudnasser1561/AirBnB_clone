#!/usr/bin/python3

import uuid #this is for the unique id generation
from datetime import datetime	

class BaseModel:
	def __init__(self, *args, **kwargs):
		
		time_format = "%Y-%m-%dT%H:%M:%S.%f" 
		if kwargs:
			for key, value in kwargs.items():
				if key == "__class__":
					continue #don't do anything
				elif key == "created_at" or "updated_at":
					setattr(self, key, datetime.strptime(value, time_format))
				else:
					setattr(self, key, value)
		else:
			self.id = str(uuid.uuid4())

		# this is the setting of the attributes of the Model
		self.id = str(uuid.uuid4())
		self.created_at = datetime.utcnow()
		self.updated_at = datetime.utcnow()
	def save(self):
		self.updated_at = datetime.utcnow()
		
	def to_dict(self):
		instance_dict = self.__dict__.copy()
		instance_dict["__class__"] = self.__class__.__name__
		instance_dict["created_at"] = self.created_at.isoformat()
		instance_dict["updated_at"] = self.updated_at.isoformat()

		return instance_dict

	
	def __str__(self): # returns a string representation of the Object
		class_name = self.__class__.__name__
		return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

if __name__ == "__main__":
	my_model = BaseModel()
	my_model.name = "My Model"
	my_model.my_number = 73
	print(my_model)
	my_model.save()
	print(my_model)
	my_model_json = my_model.to_dict()
	print(my_model_json)
	print("JSON of my_model:")
	for key in my_model_json.keys():
		print("\t{}: ({} - {})".format(key, type(my_model_json[key]), my_model_json[key]))
	
