#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6240661663:AAGu4giPfaIxNkaT4YTlnsHEnbR50ccuh68")
    API_ID = int(os.environ.get("API_ID", "29152063"))
    API_HASH = os.environ.get("API_HASH", "df3207f0fe395c1a79919d7eb311c8e4")
    AUTH_USERS = "5760012562"

