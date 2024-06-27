# LoM/MushroomADB.py
from adb_shell.adb_device import AdbDeviceTcp
from loguru import logger
from LoM.MushroomMessages import ADB_CONNECTED, ADB_FAILED, EMULATOR_CORRECT, DISPLAY_SIZE_INCORRECT, DISPLAY_DENSITY_INCORRECT, DISPLAY_CHECK_FAILED, CLICK_FAILED

def connect_adb(ip, port):
    try:
        device = AdbDeviceTcp(ip, port)
        device.connect(rsa_keys=[None], auth_timeout_s=0.1)
        logger.debug(ADB_CONNECTED)
        return device
    except Exception as e:
        logger.error(ADB_FAILED.format(error=e))
        return None

def check_display_properties(device):
    try:
        output = device.shell('wm size')
        size_check = '720x1280' in output

        output = device.shell('wm density')
        density_check = '240' in output

        return size_check, density_check
    except Exception as e:
        logger.error(DISPLAY_CHECK_FAILED.format(error=e))
        return False, False

def initialize_adb(ip, port):
    device = connect_adb(ip, port)
    if device:
        size_check, density_check = check_display_properties(device)
        if size_check and density_check:
            logger.debug(EMULATOR_CORRECT)
        else:
            if not size_check:
                logger.error(DISPLAY_SIZE_INCORRECT)
            if not density_check:
                logger.error(DISPLAY_DENSITY_INCORRECT)
        return device
    else:
        logger.error(ADB_FAILED)
        return None

def adb_click(device, x, y):
    try:
        device.shell(f'input tap {x} {y}')
    except Exception as e:
        logger.error(CLICK_FAILED.format(x=x, y=y, error=e))
