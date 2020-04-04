from nonebot.default_config import *
from os import path
import json

HOST = '172.17.0.1'
PORT = 8080

SUPERUSERS = {2801511863}
GAME_GROUPS = {959511489}
BOT_BAN = {}
COMMAND_START = {''}

"""
async def get_user_info(user_id: int) -> dict:
  user_info = {}
  user_init = {
    'money': 0,
    'checkin_time': 1,
    'elephant_bet': 0,
    'elephant_win': 0,
    'dice_bet': 0,
    'dice_income': 0,
    }
  if path.exists('data/user_info/%d.json'%user_id):
    user_info = json.loads(open('data/user_info/%d.json'%user_id).read())
  for (item, value) in user_init.items():
    if item not in user_info:
      user_info[item] = value
  return user_info

async def save_user_info(user_id: int, user_info: dict):
  with open('data/user_info/%d.json'%user_id, 'w') as user_file:
    user_file.write(json.dumps(user_info, sort_keys=True, indent=4, separators=(',', ': ')))

elephant_ingaming = {}
elephant_event = {}
elephant_info = {}
elephant_name = {}
elephant_dist = {}
dice_ingaming = {}
dice_event = {}
"""

poem_data = open("data/poem/2.txt", "r", encoding="utf-8").read().split('\n')