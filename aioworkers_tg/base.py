from aiotg import Bot
from aioworkers.core.base import AbstractEntity


class Telegram(AbstractEntity):

    def __init__(self, config=None, *, context=None, loop=None):
        super().__init__(config, context=context, loop=loop)
        self.bot = Bot(api_token=self.config.api_token)
