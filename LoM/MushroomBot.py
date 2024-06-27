# LoM/MushroomBot.py
from loguru import logger
from LoM.MushroomImages import POPUP_IMAGE, AFK_REWARD_IMAGE
from LoM.MushroomMessages import BOT_STARTED, BOT_STOPPED, USING_IMAGE, DEVICE_NOT_FOUND, SCREENSHOT_FAILED, POPUP_FOUND, CLICKING_POPUP, AFK_REWARD_FOUND, CLICKING_AFK_REWARD
from LoM.MushroomADB import initialize_adb, adb_click
from LoM.MushroomConfig import load_config
import cv2
import numpy as np
import os
import time
import threading

config = load_config()
device = initialize_adb(config["EmulatorSettings"]["ADB_IP"], config["EmulatorSettings"]["ADB_Port"])

bot_active = False

def start_bot_handler():
    global bot_active
    if device:
        bot_active = True
        bot_thread = threading.Thread(target=start_bot)
        bot_thread.start()
    else:
        logger.error(DEVICE_NOT_FOUND)

def stop_bot_handler():
    global bot_active
    bot_active = False
    stop_bot()

def start_bot():
    logger.info(BOT_STARTED)
    popup_img = cv2.imread(POPUP_IMAGE, cv2.IMREAD_GRAYSCALE)
    afk_reward_img = cv2.imread(AFK_REWARD_IMAGE, cv2.IMREAD_GRAYSCALE)
    logger.debug(USING_IMAGE.format(image_path=POPUP_IMAGE))
    logger.debug(USING_IMAGE.format(image_path=AFK_REWARD_IMAGE))
    while bot_active:
        screenshot = take_screenshot()
        if screenshot is not None:
            if check_for_popup(screenshot, popup_img):
                logger.info(POPUP_FOUND)
                click_popup()
                logger.info(CLICKING_POPUP)
            elif config["MushroomSettings"]["AFKReward"] and check_for_afk_reward(screenshot, afk_reward_img):
                logger.info(AFK_REWARD_FOUND)
                click_afk_reward()
                logger.info(CLICKING_AFK_REWARD)
        time.sleep(1)
    logger.info(BOT_STOPPED)

def take_screenshot():
    screenshot_path = 'LoM/MushroomScreen.png'
    try:
        device.shell('screencap -p /sdcard/screenshot.png')
        device.pull('/sdcard/screenshot.png', screenshot_path)
        screenshot = cv2.imread(screenshot_path, cv2.IMREAD_GRAYSCALE)
        if screenshot is None:
            logger.error(f"Failed to load screenshot from {screenshot_path}")
        return screenshot
    except Exception as e:
        logger.error(SCREENSHOT_FAILED.format(error=str(e)))
        return None

def find_subimage(screenshot, subimage):
    result = cv2.matchTemplate(screenshot, subimage, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    return max_loc, max_val

def check_for_popup(screenshot, popup_img):
    position, similarity = find_subimage(screenshot, popup_img)
    logger.debug(f"Popup detection result: {similarity} at {position}")
    return similarity > 0.8

def check_for_afk_reward(screenshot, afk_reward_img):
    position, similarity = find_subimage(screenshot, afk_reward_img)
    logger.debug(f"AFK reward detection result: {similarity} at {position}")
    return similarity > 0.8

def click_popup():
    adb_click(device, 413, 203)

def click_afk_reward():
    adb_click(device, 361, 494)

def stop_bot():
    logger.info(BOT_STOPPED)
