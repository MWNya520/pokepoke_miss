from nonebot import on_notice
from nonebot.adapters.onebot.v11 import PokeNotifyEvent, Bot, Event

import random

# 戳一戳 Matcher
poke = on_notice()

# 消息列表
message_list = [
    ("MISS",0.2),
    ("GOOD",0.2),
    ("GREAT",0.5),
    ("PERFECT",0.4),
    ("CRITICAL PERFECT",0.2)
]

@poke.handle()
async def handle_poke(bot: Bot, event: PokeNotifyEvent):
    # 确认是戳机器人自己
    if event.target_id == event.self_id:
        # 分离消息和概率
        messages, weights = zip(*message_list)
        # 根据概率选一个消息回复
        reply = random.choices(messages, weights=weights, k=1)[0]
        await poke.send(reply)
