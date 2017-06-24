# !/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable = C0103

import os
import logging
from logging.handlers import RotatingFileHandler
from logging import StreamHandler


class Logger(object):
    """
    给全局用的logger，输出到文件
    """
    LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    LOG_DEBUG = 'debug.log'
    LOG_INFO = 'info.log'
    LOG_WARNING = 'warning.log'
    LOG_ERROR = 'error.log'
    LOG_FOLDER = 'logs'
    logger = None

    def __init__(self):
        base = os.path.join(os.getcwd(), self.LOG_FOLDER)
        if not os.path.exists(base):
            os.mkdir(base)
        self.debugLogger = self.initlogger(logging.DEBUG, self.LOG_DEBUG)
        self.infoLogger = self.initlogger(logging.INFO, self.LOG_INFO)
        self.warningLogger = self.initlogger(logging.WARNING, self.LOG_WARNING)
        self.errorLogger = self.initlogger(logging.ERROR, self.LOG_ERROR)

    def debug(self, msg):
        """
        输出debug信息到文件
        """
        self.debugLogger.debug(msg)

    def info(self, msg):
        """
        输出info信息到文件
        """
        self.infoLogger.info(msg)

    def warning(self, msg):
        """
        输出warning信息到文件
        """
        self.warningLogger.warning(msg)

    def error(self, msg):
        """
        输出error信息到文件
        """
        self.errorLogger.error(msg)

    def initlogger(self, level, name):
        """
        初始化logger
        """
        cwd = os.getcwd()
        formatter = logging.Formatter(self.LOG_FORMAT)
        logger = logging.getLogger(name)
        logger.setLevel(level)
        fh = RotatingFileHandler(os.path.join(cwd, self.LOG_FOLDER, name),
                                 maxBytes=10 * 1024 * 1024,
                                 backupCount=5)
        fh.setFormatter(formatter)
        fh.setLevel(level)
        logger.addHandler(fh)
        if level is not logging.DEBUG:
            ch = StreamHandler()
            ch.setFormatter(formatter)
            ch.setLevel(level)
            logger.addHandler(ch)
        return logger
