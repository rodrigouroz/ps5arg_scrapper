import telegram
import logging
import random
from lib.sslless_session import SSLlessSession

class NullNotifier:
    def notify(self, message):
        pass

class Notifier(NullNotifier):
    def __init__(self, config, disable_ssl):
        logging.info(f"Setting up bot with token {config['token']}")
        self.config = config
        if disable_ssl:
            self.bot = telegram.Bot(token=self.config['token'], request=SSLlessSession())
        else:
            self.bot = telegram.Bot(token=self.config['token'])

    def notify(self, message):
        logging.info(f'Notifying')
        self.bot.send_message(chat_id=self.config['chat_id'], text=message)

    @staticmethod
    def get_instance(config, disable_ssl = False):
        if config['enabled']:
            return Notifier(config, disable_ssl)
        else:
            return NullNotifier()