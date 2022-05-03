"""
This file holds all the CONSTANTS the bot uses.

Copyright (c) 2022 Mathavan Pirathaban
"""

import os
import praw

#CONSTANTS
BOT_TOKEN = os.environ['BOT_TOKEN']
GIPHY_API_KEY = os.environ['GIPHY_API_KEY']
LAUGHING_WORDS = ["lol", "lmao", "lmfao", "hehe", "haha",
                 "xd"]

MOODS = ['Happy', 'Calm', 'Silly', 'Relaxed', 'Nervous',
      'Annoyed', 'Sad', 'Shy', 'Hungry', 'Angry', 'Confused',
      'Sleepy', 'Sick', 'Hurt'
      ]
SAD_WORD = "sad"
REDDIT = praw.Reddit(client_id = os.environ['PRAW_ID'],
                    client_secret = os.environ['PRAW_SECRET'],
                    username = os.environ['REDDIT_USER'],
                    password = os.environ['REDDIT_PASS'],
                    user_agent = "pythonpraw",
                    check_for_async = False
                    )

BOT_ID = "930296939675811852"
