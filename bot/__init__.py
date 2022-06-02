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

USER_SESSION = "BQBN5x0M6UI9Z7ovMMIvkF61Q2Zck9pDQNIMlqYeOAAH2g90xanaNQPXgXAddwlm7jBkZmcDxiuxMYuJJDHtALS_r-bLWIpzBWNg9M8IED-VS9CsuwPKf7wIJjIofv4FLqqkUeZy0OZPE5BAopYs_pUN837gkPL4sV37oz7DQsyMFCNM-zVYMeF4_29F8bDopnP5EjcLq8V2rJ5XkX7mql2Z-RcmL5r6dZR2SE6k1ugXBoqnvrGKDJfQCvuRLAuugF9OnHxBqqLRHWuy-PrJJRXDed-YghUJCUntFjPKyvZbift5wVFP5gIgxAyMsHNUOd-Sz1Ol9-cd4k3nOq_MT2b0QmCmWgA"

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
