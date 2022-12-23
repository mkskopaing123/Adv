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

DB_URI = "mongodb+srv://anuragb7:anuragb7@cluster0.g5kbflk.mongodb.net/?retryWrites=true&w=majority"

USER_SESSION = "BQAgT1YANRWoj9f34Eu5PuDUrhwOtTDAJWCU-TbCh8_Dti0ZhnHtden7fosnRJ5uMUMlY6Fy0sY7TwbQCU8GHmmj5cFgjzUxt8aytpvZ0Mzl7v_U8aUPixNf0j2zYfLZzUgGYHukzuyr14cxnQJ-udc-tgELnzeSBt_7yMTr8jeAYfTg0EKvIB6G2KamWwUudxi6UmG94-y00Aw5wRB7XJ7Osd1yV-dh1JOT5Hzz2SyuynT7alB6t-9IhxGXnkxgpfOLnDoejD87ui4BhUBX8krf5L_3Am_I-PQCazo8lpPmWeFQRP_jJSTKznUwTjvFh1kENm90RMk7XtOL2Qr33eAuHse7fAAAAABCYKZaAA"

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
