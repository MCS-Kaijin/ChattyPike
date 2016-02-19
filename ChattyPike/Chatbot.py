import re

from CategoryObj import *

class ChatBot:
	def __init__(self, brain, name, gender, age):
		self.brain = brain
		self.name = name
		self.gender = gender
		self.age = str(age)
	
	def respond(self, text):
		for category in self.brain:
			p = category.pattern
			condition = False
			if type(p) == StrictPattern: condition = re.match(p.value, text)
			else: condition = re.search(p.value, text)
			if condition:
				return category.template.choose()