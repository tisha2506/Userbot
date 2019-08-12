# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot initialization. """

import os

from sys import version_info
from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb

from dotenv import load_dotenv
from requests import get
from telethon import TelegramClient
from telethon.sessions import StringSession

load_dotenv("config.env")

# Bot Logs setup:
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))


if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=INFO
    )
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 6:
    LOGS.error(
        "You MUST have a python version of at least 3.6."
        " Multiple features depend on this. Bot quitting."
    )
    quit(1)

# Check if the config was edited by using the already used variable
CONFIG_CHECK = os.environ.get("", None)

if CONFIG_CHECK:
    LOGS.error("Please remove the line mentioned in the first hashtag from the config.env file")
    quit(1)


API_KEY = os.environ.get("API_KEY", '968293')

API_HASH = os.environ.get("API_HASH", '55102ff3b70df1826e1832506b6b2909')

STRING_SESSION = os.environ.get("STRING_SESSION", None)

BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", "0"))

BOTLOG = sb(os.environ.get(
    "BOTLOG", "False"
))

PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))

CONSOLE_LOGGER_VERBOSE = sb(
    os.environ.get("CONSOLE_LOGGER_VERBOSE", "False")
    )

DB_URI = os.environ.get("DATABASE_URL", None)

OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)

GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)

SCREENSHOT_LAYER_ACCESS_KEY = os.environ.get(
    "SCREENSHOT_LAYER_ACCESS_KEY", None
    )

OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)

WELCOME_MUTE = sb(os.environ.get(
    "WELCOME_MUTE", "False"
))

YOUTUBE_API_KEY = os.environ.get(
    "YOUTUBE_API_KEY", None
    )

# Spotify Bio

SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME", None)
SPOTIFY_PASS = os.environ.get("SPOTIFY_PASS", None)
SPOTIFY_BIO_PREFIX = os.environ.get("SPOTIFY_BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)

# GDrive Module

G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")

if STRING_SESSION:
    # pylint: disable=invalid-name
    bot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
else:
    # pylint: disable=invalid-name
    bot = TelegramClient("userbot", API_KEY, API_HASH)


# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
ENABLE_KILLME = True
CMD_HELP = {}
ZALG_LIST = [["̖",
              " ̗",
              " ̘",
              " ̙",
              " ̜",
              " ̝",
              " ̞",
              " ̟",
              " ̠",
              " ̤",
              " ̥",
              " ̦",
              " ̩",
              " ̪",
              " ̫",
              " ̬",
              " ̭",
              " ̮",
              " ̯",
              " ̰",
              " ̱",
              " ̲",
              " ̳",
              " ̹",
              " ̺",
              " ̻",
              " ̼",
              " ͅ",
              " ͇",
              " ͈",
              " ͉",
              " ͍",
              " ͎",
              " ͓",
              " ͔",
              " ͕",
              " ͖",
              " ͙",
              " ͚",
              " ",
              ],
             [" ̍",
              " ̎",
              " ̄",
              " ̅",
              " ̿",
              " ̑",
              " ̆",
              " ̐",
              " ͒",
              " ͗",
              " ͑",
              " ̇",
              " ̈",
              " ̊",
              " ͂",
              " ̓",
              " ̈́",
              " ͊",
              " ͋",
              " ͌",
              " ̃",
              " ̂",
              " ̌",
              " ͐",
              " ́",
              " ̋",
              " ̏",
              " ̽",
              " ̉",
              " ͣ",
              " ͤ",
              " ͥ",
              " ͦ",
              " ͧ",
              " ͨ",
              " ͩ",
              " ͪ",
              " ͫ",
              " ͬ",
              " ͭ",
              " ͮ",
              " ͯ",
              " ̾",
              " ͛",
              " ͆",
              " ̚",
              ],
             [" ̕",
              " ̛",
              " ̀",
              " ́",
              " ͘",
              " ̡",
              " ̢",
              " ̧",
              " ̨",
              " ̴",
              " ̵",
              " ̶",
              " ͜",
              " ͝",
              " ͞",
              " ͟",
              " ͠",
              " ͢",
              " ̸",
              " ̷",
              " ͡",
              ]]
