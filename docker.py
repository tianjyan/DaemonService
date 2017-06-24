# !/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable = C0111
# pylint: disable = C0103

import os
import json
from itty import run_itty
from itty import post
from common.logger import Logger
from bots.chat import SparkChatBot

HOST = '0.0.0.0'
PORT = 8080


@post('/spark-bot')
def spark(request):
    return chatBot.webhookRequest(request)


logger = Logger()
logger.info(u'Logger初始化完成')
logger.info(u'读取配置文件')
confileFileName = 'config.json'
env = os.environ.get('ENV')
if env == "DEV":
    confileFileName = 'config.dev.json'
configFile = file(confileFileName)
config = json.load(configFile)
configFile.close()
logger.info(u'读取配置文件完成')
chatBot = SparkChatBot(logger, config['bearer'])
logger.info(u'启动 itty')
run_itty(server='wsgiref', host=HOST, port=PORT)
