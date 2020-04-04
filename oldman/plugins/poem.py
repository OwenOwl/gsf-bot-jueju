from nonebot import on_command, CommandSession
import random
from config import *

async def sentence(L: int) -> str:
  f = poem_data
  s = ""
  while len(s) < L:
    t = random.choice(f)
    if len(s) + len(t) <= L:
      s = s + t
  return s

async def ct() -> str:
  c = random.randint(1, 10)
  if c == 1:
    return "？"
  elif c <= 3:
    return "！"
  else:
    return "。"

async def get_poem(L: int, title: str) -> str:
  s = ""
  s = s + "《" + title + "》" + "\n"
  s = s + await sentence(L) + "，" + "\n"
  s = s + await sentence(L) + await ct() + "\n"
  s = s + await sentence(L) + "，" + "\n"
  s = s + await sentence(L) + await ct()
  return s

@on_command('绝句', only_to_me=False)
async def poem(session: CommandSession):
  if session.ctx.get('group_id') in BOT_BAN:
    return
  L = random.choice([5, 7])
  title = session.get('title')
  if len(title) > 10:
    await session.send('标题太长')
    return
  poem_result = await get_poem(L, title)
  if session.ctx.get('group_id'):
    await session.send('[CQ:at,qq=%d]\n'%session.ctx['user_id'] + poem_result)
  else:
    await session.send(poem_result)


@poem.args_parser
async def _(session: CommandSession):
  stripped_arg = session.current_arg_text.strip().split('\r')[0]

  if session.is_first_run:
    if stripped_arg:
      session.state['title'] = stripped_arg
    else:
      session.state['title'] = await sentence(random.randint(1, 5))
    return

  if not stripped_arg:
    session.pause('ERR')

  session.state[session.current_key] = stripped_arg