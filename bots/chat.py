# !/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable = C1001
# pylint: disable = C0111
# pylint: disable = C0103
# pylint: disable = W0703

import json
from bots.abcbot import ABCBot
from chatterbot import ChatBot


class SparkChatBot(ABCBot):

    BOTEMAIL = 'bot.ytj@sparkbot.io'
    BOTNAME = 'Tianjie\'s Bot'
    BOTTRAINER = 'chatterbot.trainers.ChatterBotCorpusTrainer'
    BOTLANGUAGE = 'chatterbot.corpus.english'

    chatbot = None

    def __init__(self, logger, bearer):
        super(SparkChatBot, self).__init__(logger, bearer)
        self.logger = logger
        self.chatbot = ChatBot(self.BOTNAME, trainer=self.BOTTRAINER)
        self.chatbot.train(self.BOTLANGUAGE)

    def webhookRequest(self, request):
        webhook = json.loads(request.body)
        email = webhook['data']['personEmail']
        if email != self.BOTEMAIL:
            self.logger.info('user email: {0}'.format(email))
            result = self.getMessageContent(webhook['data']['id'])
            result = json.loads(result)
            text = result.get('text', '').lower()
            self.logger.info('request: {0}'.format(text.encode('utf-8')))
            responseContent = self.chatbot.get_response(text.encode('ascii', 'ignore'))
            self.logger.info('response: {0}'.format(str(responseContent).encode('utf-8')))
            self.postMessage(webhook['data']['roomId'], str(responseContent))
        return 'true'
