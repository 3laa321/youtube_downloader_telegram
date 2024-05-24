import os
from telebot import TeleBot
from telebot.types import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
from telebot import types
from KeyboardButton import * 
from language import *
import requests
from pytube import YouTube
import uuid
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC, error
from mutagen.mp3 import MP3
from pydub import AudioSegment
from tqdm import tqdm


# ------------imports-----------
commands = [
		BotCommand("start", "start bot"),
		BotCommand("language", "set language")
]

# ------------commands-----------
ICON_PATH = 'Base/icon.jpg'
bot = TeleBot("7160290004:AAF-sGOudf0CFwvJc2zec27GXITgbsOof2o")
bot.set_my_commands(commands)
