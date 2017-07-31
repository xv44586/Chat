from chatterbot import ChatBot
from .helper import my_train


class Bot(object):
    bot = ChatBot(my_train.model_name)

    def get_answer(self, question_test):
        return self.bot.get_response(question_test)

my_bot = Bot()