#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(2117462)

API_HASH = "0b5076987398769334ad1f7b439f2562"

BOT_TOKEN = "5806016246:AAE_C1NtmjSpgFRk8pd1v0nHbOkFbVxHn8k"

DB_URI = "mongodb+srv://erichdaniken:erichdaniken@cluster0.rzdg1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

USER_SESSION = "BQClAi7oj12iKsFaqsOW06wFiOEdfYAYL7GXdjoM7aKOtq_IGkMt4mtYUWp9YGfB_V9ylgRA3hNTHVaAgrGqvWXYG69VJqkZvN-7p5XxB6sF-6KANBtUzATv1vReqc2KZEdY8w-vdLzHBVpAB0WsFd17X4wuy1xZZ0x85QfF9YoOitZOYrxwWS0smoq9CtLbdzzfLnNTpAyfFqxIi4wuNBV7WhouNvwG0q-_u3YmfyW0XC_Z0hYYZB78rF3LvyOyuOSNnkkcRLG53GZosDK_uvYqyIVc8VkeRVuirp11DRXs7sbirKyhPKTCWXPEcX4Has2rLKeczOGAvq-8CmKrAdbIQmCmWgA"

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
