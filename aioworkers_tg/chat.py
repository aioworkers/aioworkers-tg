from aioworkers_tg.bot import TelegramBot


class TelegramChat(TelegramBot):

    def __init__(self, config=None, *, context=None, loop=None):
        super().__init__(config, context=context, loop=loop)

        if self.config.get('user_id'):
            self.chat = self.bot.channel(self.config.user_id)
        elif self.config.get('group_id'):
            self.chat = self.bot.group(self.config.group_id)
        elif self.config.get('channel'):
            self.chat = self.bot.channel(self.config.channel)

        assert self.chat

    async def send_text(self, text):
        await self.chat.send_text(text)
