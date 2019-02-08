from aiotg import Bot
from aioworkers.core.base import AbstractEntity


class TelegramBot(AbstractEntity):
    # Methods of aiotg.Bot which will be bind to entity
    __bind_methods = (
        'group',
        'channel',
        'private',
    )

    def __init__(self, config=None, *, context=None, loop=None):
        super().__init__(config, context=context, loop=loop)
        bot = self.config.get('bot')
        if bot:
            self.bot = self.context[bot]
        else:
            self.bot = Bot(api_token=self.config.api_token)

        for method_name in self.__bind_methods:
            f = getattr(self.bot, method_name)
            if f:
                setattr(self, method_name, f)
