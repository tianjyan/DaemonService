# !/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable = C1001
# pylint: disable = C0111
# pylint: disable = C0103
# pylint: disable = W0703
# pylint: disable = C0301

import urllib2
import json
from bots.abcbot import ABCBot

class BingWallpaperBot(ABCBot):
    BINGURL = 'http://bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1439260838289&pid=hp&video=1'

    def __init__(self, logger, bearer):
        super(BingWallpaperBot, self).__init__(logger, bearer)

    def webhookRequest(self, request):
        webhook = json.loads(request.body)
        content = self.getMessageContent(webhook['data']['id'])
        content = json.load(content)
        if 'tianjie\'s' in content.get('text', 'bingwallpaper').lower():
            items = content.get('text').split()
            if len(items) == 2 and items[1] == u'':
                self.sendBingImage(webhook['data']['roomId'])
        elif u'bingwallpaper' in content.get('text', '').lower():
            self.sendBingImage(webhook['data']['roomId'])

    def getBingImageUrl(self):
        url = None
        try:
            request = urllib2.Request(self.BINGURL)
            response = urllib2.urlopen(request)
            content = response.read()
            result = json.loads(content)
            url = result['images'][0]['url']
            self.logger(url)
        except Exception as e:
            self.logger(e.message)
        return url

    def sendBingImage(self, roomId):
        url = self.getBingImageUrl()
        self.postFile(roomId, url)
