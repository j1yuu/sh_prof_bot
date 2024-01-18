import logging

def loggerInit():

    logger = logging.getLogger('aiogram.dispatcher')
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d [%(filename)s])')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # handler = logging.FileHandler('Logs/aiogram.log', encoding='utf-8')
    # handler.setLevel(logging.DEBUG)
    # formatter = logging.Formatter('%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d [%(filename)s])')
    # handler.setFormatter(formatter)
    # logger.addHandler(handler)