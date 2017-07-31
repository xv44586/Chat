from chatterbot import ChatBot

from helper import my_train

data = ["嗳，渡边君，真喜欢我?",
    "那还用说?",
    "那么，可依得我两件事?",
    "三件也依得",
        ]

my_train.train(data)
my_train.train(['这个是没训练的', '这样呢', '偶数呢', 'so what'])
my_train.train(['九章', '大财团啊那是'])
def test(text):
    reply_chatbot = ChatBot(my_train.model_name)
    print(reply_chatbot.get_response(text))

test('hi')
test('嗳，渡边君')
test('图')
