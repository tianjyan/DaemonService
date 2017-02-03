# !/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable = C1001
# pylint: disable = C0111
# pylint: disable = C0103
# pylint: disable = W0703

import urllib2
import json

class ABCBot(object):
    logger = None
    MSGURL = 'https://api.ciscospark.com/v1/messages/'

    def __init__(self, logger, bearer):
        self.logger = logger
        self.BEARER = bearer
        self.HEADERS = {'Accept' : 'application/json', \
                'Content-Type' : 'application/json', \
                'Authorization' : 'Bearer ' + self.BEARER}

    def getMessageContent(self, msgId):
        request = urllib2.Request('{}/{}'.format(self.MSGURL, msgId), headers=self.HEADERS)
        contents = urllib2.urlopen(request).read()
        return contents

    def post(self, responseBody):
        request = urllib2.Request(self.MSGURL, json.dumps(responseBody), headers=self.HEADERS)
        contents = urllib2.urlopen(request).read()
        return contents

    def postMessage(self, roomId, message):
        responseBoday = {'roomId': roomId, 'text': message}
        self.post(responseBoday)

    def postFile(self, roomId, fileUrl):
        responseBody = {'roomId': roomId, 'files': fileUrl}
        self.post(responseBody)
