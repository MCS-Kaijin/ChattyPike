from random import choice

BRAIN = []

class Category:
	def __init__(self, pattern, template):
		self.pattern = pattern
		self.template = template
		BRAIN.append(self)

# patterns classes
class StrictPattern:
	def __init__(self, value):
		self.value = value

class LoosePattern:
	def __init__(self, value):
		self.value = value


# response classes
class SimpleResponse(str):
	def choose(self):
		return self

class RandomResponse(list):
	def choose(self):
		return choice(self)