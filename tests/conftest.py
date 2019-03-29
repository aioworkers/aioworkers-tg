import pytest


@pytest.fixture
def config_yaml():
    return """
    bot:
      cls: aioworkers_tg.bot.TelegramBot
      api_token: 1234567890
    """


@pytest.fixture
def api_call(mocker):
    from aiohttp.test_utils import make_mocked_coro
    mock = mocker.patch(
        'aiotg.bot.Bot.api_call',
        make_mocked_coro()
    )
    yield mock
