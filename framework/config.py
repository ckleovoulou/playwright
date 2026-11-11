"""Central configuration. Values come from environment variables (or .env) with safe defaults."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class User:
    username: str
    password: str


# Sauce Demo publishes these demo accounts on its login page.
PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")
STANDARD_USER = User(os.getenv("SAUCE_USER", "standard_user"), PASSWORD)
LOCKED_OUT_USER = User("locked_out_user", PASSWORD)

# Mobile
APPIUM_SERVER = os.getenv("APPIUM_SERVER", "http://127.0.0.1:4723")
APP_PATH = os.getenv("APP_PATH", "apps/ApiDemos-debug.apk")
ANDROID_DEVICE_NAME = os.getenv("ANDROID_DEVICE_NAME", "Android Emulator")
