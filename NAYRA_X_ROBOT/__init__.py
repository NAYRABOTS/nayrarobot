from NAYRA_X_ROBOT.core.bot import JARVIS
from NAYRA_X_ROBOT.core.dir import dirr
from NAYRA_X_ROBOT.core.git import git
from NAYRA_X_ROBOT.core.userbot import Userbot
from NAYRA_X_ROBOT.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = JARVIS()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
