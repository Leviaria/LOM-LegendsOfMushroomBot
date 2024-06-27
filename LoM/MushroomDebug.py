# LoM/MushroomDebug.py
from adb_shell.adb_device import AdbDeviceTcp
from PIL import Image
import io

def connect_adb(ip, port):
    try:
        device = AdbDeviceTcp(ip, port)
        device.connect(rsa_keys=[None], auth_timeout_s=0.1)
        return device
    except Exception as e:
        print(f"Failed to establish ADB connection: {e}")
        return None

def capture_screenshot(device):
    try:
        raw_screenshot = device.shell('screencap -p', decode=False)
        screenshot = Image.open(io.BytesIO(raw_screenshot))
        grayscale_screenshot = screenshot.convert("L")
        grayscale_screenshot.save("screenshot_grayscale.png")
        print("Screenshot captured and saved as screenshot_grayscale.png")
    except Exception as e:
        print(f"Failed to capture screenshot: {e}")

if __name__ == "__main__":
    device = connect_adb("127.0.0.1", 5555)
    if device:
        capture_screenshot(device)
