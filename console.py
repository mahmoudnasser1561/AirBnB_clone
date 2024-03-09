#!/usr/bin/python3

import cmd
import re
import json
from models.base_model import BaseModel
from models import storage


class HBNB(cmd.Cmd):
	""" This is the class for the command interpreter """
	prompt = "(hbnb) "
