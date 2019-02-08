from .base import TelegramBot  # noqa
from .chat import TelegramChat  # noqa

try:
    from .version import __version__
except ImportError:
    __version__ = 'dev'
