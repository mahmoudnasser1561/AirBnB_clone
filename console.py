#!/usr/bin/python3

import cmd
import json

class HBNBCommand(cmd.Cmd):
	"""
		
	"""
	prompt = "(hbnb) "
	
	def do_quit(self, arg):
		"""
		"""
		return True
	def help_quit(self, args):
		print("Quit command to exit the program")

	def do_EOF(self, arg):
		"""
		
		"""
		print()
		return True

if __name__ == "__main__":
	HBNBCommand().cmdloop()
