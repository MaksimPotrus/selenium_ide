import inspect
import logging

import pytest


class LoggerABM:
    @staticmethod
    def sample_logger(logLevel=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        file_hendler = logging.FileHandler("logging_of_the_ABM.log", mode='w')
        # create format of the logs
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        # add formatter to console
        file_hendler.setFormatter(formatter)
        # add console handler
        logger.addHandler(file_hendler)
        return logger


def verify(condition, fail_message, success_message=''):
    logger = LoggerABM.sample_logger(logLevel=logging.ERROR)
    if condition:
        print('[SUCCESS]:' + success_message)
        logger.info('[SUCCESS]:' + success_message)
    else:
        print('[!<<<<<!ERROR]:' + fail_message)
        logger.info('[!<<<<<!ERROR]:' + fail_message)
