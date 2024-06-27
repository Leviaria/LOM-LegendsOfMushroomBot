# main.py
from LoM.MushroomGUI import launch_app
from LoM.MushroomConfig import create_config, load_config

create_config()
config = load_config()
launch_app()