from aioworkers_tg.base import Telegram


class TelegramGroup(Telegram):

    def __init__(self, config=None, *, context=None, loop=None):
        super().__init__(config, context=context, loop=loop)
        self.chat = self.bot.group(self.config.group_id)

    async def send_text(self, text):
        await self.chat.send_text(text)
