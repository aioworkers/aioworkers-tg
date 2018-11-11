from aiohttp.test_utils import make_mocked_coro


async def test_group(context, mocker):
    mock = mocker.patch(
        'aiotg.bot.Bot.api_call',
        make_mocked_coro()
    )
    await context.group.send_text('text')

    assert mock.call_count == 1
    c = mock.call_args_list[0]
    assert c[0] == ('sendMessage',)
    assert c[1] == {'chat_id': context.config.group.group_id, 'text': 'text'}
