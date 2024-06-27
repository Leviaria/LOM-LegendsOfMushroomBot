# LoM/MushroomMessages.py
from loguru import logger

CONFIG_EXISTS = "Config file already exists at {config_path}"
CONFIG_CREATED = "Config file created at {config_path}"
CONFIG_CORRUPT = "Config file is corrupt: {error}. Please delete the config.json file and restart the bot."
LEGENDS_CLOSED = "Legends of Mushroom has been closed."
LEGENDS_TERMINATED = "Legends of Mushroom has been terminated."

ADB_CONNECTED = "ADB connection established successfully."
ADB_FAILED = "Failed to establish ADB connection: {error}"
EMULATOR_CORRECT = "The emulator has the correct settings. The bot is ready to start."
DISPLAY_SIZE_INCORRECT = "Incorrect display size. Expected 720x1280."
DISPLAY_DENSITY_INCORRECT = "Incorrect display density. Expected 240 DPI."
DISPLAY_CHECK_FAILED = "Failed to check display properties: {error}"
CLICK_FAILED = "Failed to execute click at ({x}, {y}): {error}"
DEVICE_NOT_FOUND = "No ADB device found."
SCREENSHOT_FAILED = "Failed to take screenshot: {error}"
POPUP_FOUND = "Popup found"
CLICKING_POPUP = "Clicking popup at (413, 203)"
AFK_REWARD_FOUND = "AFK reward found"
CLICKING_AFK_REWARD = "Clicking AFK reward at (361, 494)"

BOT_STARTED = "Bot started."
BOT_STOPPED = "Bot stopped."
USING_IMAGE = "Using image: {image_path}"

CONFIG_FILE_NOT_FOUND = "Config file not found at {config_path}. Creating a new config file."
CONFIG_ERROR_READING = "Error reading config file: {error}"
CONFIG_ERROR_CREATING = "Failed to create config file: {error}"
