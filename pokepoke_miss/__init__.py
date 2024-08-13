from nonebot import on_notice
from nonebot.adapters.onebot.v11 import PokeNotifyEvent, Bot, Event
from nonebot.plugin import PluginMetadata

import random

# 戳一戳 Matcher
poke = on_notice(priority=100,block=False)

# 消息列表

# 预设方案①
'''
message_list = [
    ("MISS",0.2),
    ("GOOD",0.2),
    ("GREAT",0.5),
    ("PERFECT",0.4),
    ("CRITICAL PERFECT",0.2)
]
'''

# 预设方案②
message_list = [
    ("嗝~绝赞都被我吃完惹！MISS！",0.2),
    ("绝赞都快要吃完了，你怎么才来拍我……只能给你 GOOD 惹",0.2),
    ("才吃一半，爆个粉，给你个 GREAT 吧~",0.5),
    ("还没有吃掉绝赞，你抓住了Break，就给你 PERFECT 吧！",0.4),
    ("还没看见绝赞，就被你抓走了……给你 CRITICAL PERFECT 的评价~！",0.2)
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
