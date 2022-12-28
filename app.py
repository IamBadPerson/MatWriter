import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.label import Label

from loguru import logger

logger.add('log.log')

class Writer(App):

    def build(self):
        return Label(text='test')

if __name__ == '__main__':
    logger.info('starting up spin')
    Writer().run()