from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('BotAtlas')
conv_1 = ['oi','olá','como vai','Bom dia','Boa tarde','Boa noite','Boa noite','Bom dia, '
          'como vai?','Boa tarde, como vai?','Boa noite, como vai?', 'estou bem']

bot.set_trainer(ListTrainer)
bot.train(conv_1)

while True:
        quest = input('Você: ')
        response = bot.get_response(quest)
        print('Bot: ', response)
