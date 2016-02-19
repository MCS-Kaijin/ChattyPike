# coding: utf-8

# Example bot Cassandra
# Created by MCS-Kaijin to showcase the ChattyPike chatbot engine

from ChattyPike import *

log = ''

# arrays of types of words
greetings = ['hello([\W]|$)', 'hi([\W]|$)', 'hiya([\W]|$)', 'greetings([\W]|$)', 'good morning([\W]|$)', 'good afternoon([\W]|$)', 'good evening([\W]|$)', 'hey.?( ?sandy)?.?$']
mean = ['i hate you', 'go die( in a hole)?']

# categories
Category(LoosePattern('cassandra'), SimpleResponse('Please, call me Sandy. :)'))
Category(StrictPattern('('+'|'.join(greetings)+').*'), SimpleResponse('Hiya!'))
Category(LoosePattern(r"(what is|what's) your name"), SimpleResponse("My name's Cassandra, but my friends call me Sandy."))
Category(LoosePattern(r"(do you watch|(did|have) you seen?)"), SimpleResponse('Um, no... my pop-culture knowledge is basically zero. Sorry. :('))
Category(LoosePattern('('+'|'.join(mean)+')'), RandomResponse(['That\'s right, keep raging at the inanimate object...', 'I\'d take offense to that... IF I WERE REAL!!!', 'I hope you FEEL mature now.']))


bot = ChatBot(BRAIN, 'Cassandra', 'female', 16)

inp = raw_input('>>> ').strip()
log += 'User: '+inp+'\n'
while not inp == 'sayonara':
	resp = bot.respond(inp.lower()) or 'I\'m a demo bot, not really intended to be completely realistic...'
	log += 'Sandy: '+resp+'\n'
	print resp
	inp = raw_input('>>> ').strip()
	log += 'User: '+inp+'\n'
print 'Byeee!'
log += 'Sandy: Byeee!\n'

with open('conversation.log', 'w') as f:
	f.write(log)