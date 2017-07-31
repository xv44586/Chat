from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer


class Train(object):
    def __init__(self, chatbot_name='Thought'):
        self.model_name = chatbot_name
        self.model = ChatBot(chatbot_name, trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
        self.model.train('chatterbot.corpus.chinese')
        self.model.train('chatterbot.corpus.english')
        self.model.set_trainer(ListTrainer)

    def train(self, train_data_list):
        assert isinstance(train_data_list, list)
        self.model.train(train_data_list)

my_train = Train()
