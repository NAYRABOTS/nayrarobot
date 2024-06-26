import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from NAYRA_X_ROBOT import LOGGER, app, userbot
from NAYRA_X_ROBOT.core.call import JARVIS
from NAYRA_X_ROBOT.misc import sudo
from NAYRA_X_ROBOT.plugins import ALL_MODULES
from NAYRA_X_ROBOT.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐒𝐞𝐬𝐬𝐢𝐨𝐧")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("NAYRA_X_ROBOT.plugins" + all_module)
    LOGGER("NAYRA_X_ROBOT.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")
    await userbot.start()
    await JARVIS.start()
    try:
        await JARVIS.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("NAYRA_X_ROBOT").error(
            "𝗣𝗹𝗭 𝗦𝗧𝗔𝗥𝗧 𝗬𝗢𝗨𝗥 𝗟𝗢𝗚 𝗚𝗥𝗢𝗨𝗣 𝗩𝗢𝗜𝗖𝗘𝗖𝗛𝗔𝗧\𝗖𝗛𝗔𝗡𝗡𝗘𝗟\n\nJARVIS� 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣........"
        )
        exit()
    except:
        pass
    await JARVIS.decorators()
    LOGGER("NAYRA_X_ROBOT").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ☠︎𝐌𝐀𝐃𝐄 𝐁𝐘 𝐕𝐈𝐂𝐊𝐘 𝐂𝐇𝐎𝐔𝐃𝐇𝐀𝐑𝐘☠︎︎\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("NAYRA_X_ROBOT").info("𝐒𝐓𝐎𝐏 𝐏𝐀𝐊𝐇𝐈 𝐌𝐔𝐒𝐈𝐂 𝐁𝐎𝐓 ..")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
