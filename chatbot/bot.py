from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#开始时，先用chatterbot做一个简单的机器人。后面如果有机会会尝试写一个自己的机器人。
class Yuki:
    chatbot = ChatBot(
        'Yuki',
        database = './chatbot/yuki.json'
    )
    def __init__(self):
        self.chatbot.set_trainer(ChatterBotCorpusTrainer)
        #self.chatbot.train("chatterbot.corpus.chinese")
        self.chatbot.train("chatterbot.corpus.english")

    def getResponse(self, message=""):
        return str(self.chatbot.get_response(message))
