from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chat = ChatBot('myBot')
chat.set_trainer(ChatterBotCorpusTrainer)

chat.train("chatterbot.corpus.english")

print(chat.get_response("hello"))
print(chat.get_response('what is your name?'))