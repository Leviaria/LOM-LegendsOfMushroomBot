# LoM/MushroomBot.py
from loguru import logger
from LoM.MushroomImages import AFK_REWARD_IMAGE, POPUP_IMAGE
from LoM.MushroomMessages import BOT_STARTED, BOT_STOPPED, USING_IMAGE
from LoM.MushroomADB import initialize_adb
from LoM.MushroomConfig import load_config

config = load_config()
device = initialize_adb(config["EmulatorSettings"]["ADB_IP"], config["EmulatorSettings"]["ADB_Port"])

def start_bot_handler():
    if device:
        start_bot()

def stop_bot_handler():
    stop_bot()

def start_bot():
    logger.info(BOT_STARTED)
    logger.debug(USING_IMAGE.format(image_path=AFK_REWARD_IMAGE))
    logger.debug(USING_IMAGE.format(image_path=POPUP_IMAGE))

def stop_bot():
    logger.info(BOT_STOPPED)