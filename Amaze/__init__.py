from Amaze.core.bot import ALPHA
from Amaze.core.dir import dirr
from Amaze.core.git import git
from Amaze.core.userbot import Userbot
from Amaze.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = ALPHA()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
