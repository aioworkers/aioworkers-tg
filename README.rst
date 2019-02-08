aioworkers-tg
=============

.. image:: https://travis-ci.org/aioworkers/aioworkers-tg.svg?branch=master
  :target: https://travis-ci.org/aioworkers/aioworkers-tg

.. image:: https://img.shields.io/pypi/v/aioworkers-tg.svg
  :target: https://pypi.python.org/pypi/aioworkers-tg


Plugin to work with `Telegram` in `aioworkers`.

Features:

*  Telegram user.
*  Telegram channels.
*  Telegram groups.


Usage
-----

Install it with pip:

.. code:: sh

    pip install aioworkers-tg


Create entity of bot in aioworkers config:

.. code-block:: yaml

    bot:
        cls: 'aioworkers_tg.bot.TelegramBot'
        api_token: '1234567890'

You can use it directly from context:

.. code-block:: python

    await context.bot.channel('@yourchannel').send_text("Hello from channel!")


Also it is possible to create chat instance and send messages directly:

.. code-block:: yaml

    chat:
        cls: 'aioworkers_tg.chat.TelegramChat'
        bot: 'bot' # reference to created bot
        group_id: '11111'


.. code-block:: python

    await context.chat.send_text("Hello!")

