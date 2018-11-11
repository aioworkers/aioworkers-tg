import pytest


@pytest.fixture
def config():
    from aioworkers.core.config import Config
    return Config(
        group={
            'cls': 'aioworkers_tg.group.TelegramGroup',
            'api_token': '1234567890',
            'group_id': '1',
        },
    )


@pytest.fixture
def context(config, loop):
    from aioworkers.core.context import Context
    with Context(config, loop=loop) as ctx:
        yield ctx
