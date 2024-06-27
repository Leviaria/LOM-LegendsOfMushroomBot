# LoM/MushroomConfig.py
import json
import os
from loguru import logger
from LoM.MushroomMessages import (
    CONFIG_EXISTS,
    CONFIG_CREATED,
    CONFIG_CORRUPT,
    CONFIG_FILE_NOT_FOUND,
    CONFIG_ERROR_READING,
    CONFIG_ERROR_CREATING
)

DEFAULT_CONFIG = {
    "EmulatorSettings": {
        "ADB_IP": "127.0.0.1",
        "ADB_Port": 5555
    },
    "MushroomSettings": {
        "AFKReward": True
    }
}

def create_config():
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.json')
    
    if not os.path.exists(config_path):
        try:
            with open(config_path, 'w') as config_file:
                json.dump(DEFAULT_CONFIG, config_file, indent=4)
            logger.info(CONFIG_CREATED.format(config_path=config_path))
        except IOError as e:
            logger.error(CONFIG_ERROR_CREATING.format(error=e))
    else:
        logger.info(CONFIG_EXISTS.format(config_path=config_path))

def load_config():
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.json')
    
    try:
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
        
        logger.remove()
        
        logs_dir = os.path.join(os.path.dirname(__file__), 'logs')
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        
        log_file_path = os.path.join(logs_dir, 'debug.log')
        logger.add(log_file_path, level="DEBUG", format="{time} | {level} | {message}")
        logger.add(lambda msg: print(msg, end=""), level="DEBUG", format="{time} | {level} | {message}")
        
        updated = False
        for section, settings in DEFAULT_CONFIG.items():
            if section not in config:
                config[section] = settings
                updated = True
            else:
                for key, value in settings.items():
                    if key not in config[section]:
                        config[section][key] = value
                        updated = True

        if updated:
            with open(config_path, 'w') as config_file:
                json.dump(config, config_file, indent=4)
            logger.info(CONFIG_CREATED.format(config_path=config_path))

        return config
    except FileNotFoundError:
        logger.warning(CONFIG_FILE_NOT_FOUND.format(config_path=config_path))
        create_config()  # Create a new config file if it doesn't exist
        return load_config()  # Try loading again after creating
    except (json.JSONDecodeError, KeyError) as e:
        logger.error(CONFIG_CORRUPT.format(error=e))
        return None
    except IOError as e:
        logger.error(CONFIG_ERROR_READING.format(error=e))
        return None
