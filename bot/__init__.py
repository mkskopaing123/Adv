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

BOT_TOKEN = "5482704567:AAH4hOppkPz71lO4MePmSw5kbkHGkWYzVKE"

DB_URI = "mongodb+srv://erichdaniken:erichdaniken@cluster0.rzdg1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

USER_SESSION = "BQB9OL9XOOyRHkkKT5K_JF8tJrWR6Y0usYSW8_v3R2sSFfLeIdxWqEtL35gvvMKViuYf2sX2spK4nL790iiLNGyYcJmZ5MGcAPj1YU8-DXPClVM9ztf0x5t2M76rnF2RNznWkmFnw4PtUX0HeyE4PbfDkN6adVKlRYlBDuFSFrDuzSCM0T6hzeSnwM2dP8j2Jjzq_1_k8dv2iYzrn2fGdmChxqm9Qu25imiKHEf5ilUD0kvoYTro1CHa7tbkd8Gd2XF2zwA8pgzfWRr_MjeHdhIzAvIqHmOGPrJabJHyTGITfgxUA1xW5VIcLO-4UkslU720v3C2_lU6Av6ljtD27XYlQmCmWgA"

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
