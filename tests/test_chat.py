import pytest


@pytest.fixture
def config(config):
    config.update(
        group={
            'cls': 'aioworkers_tg.TelegramChat',
            'bot': 'bot',
            'group_id': '1',
        },
        user={
            'cls': 'aioworkers_tg.TelegramChat',
            'bot': 'bot',
            'user_id': '2',
        },
        channel={
            'cls': 'aioworkers_tg.TelegramChat',
            'bot': 'bot',
            'channel': '@channel',
        },
    )
    return config


async def test_group_send_text(context, api_call):
    await context.group.send_text('text')

    assert api_call.call_count == 1
    c = api_call.call_args_list[0]
    assert c[0] == ('sendMessage',)
    assert c[1] == {'chat_id': '1', 'text': 'text'}


async def test_user_send_text(context, api_call):
    await context.user.send_text('text')

    assert api_call.call_count == 1
    c = api_call.call_args_list[0]
    assert c[0] == ('sendMessage',)
    assert c[1] == {'chat_id': '2', 'text': 'text'}


async def test_channel_send_text(context, api_call):
    await context.channel.send_text('text')

    assert api_call.call_count == 1
    c = api_call.call_args_list[0]
    assert c[0] == ('sendMessage',)
    assert c[1] == {'chat_id': '@channel', 'text': 'text'}
