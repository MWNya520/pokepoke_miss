from nonebot import on_notice, on_command
from nonebot.adapters.onebot.v11 import PokeNotifyEvent, Bot, Event

import random

help = on_command("pokehelp")

@help.handle()
async def handle_help():
    await help.send(f"pokepoke_miss\n戳一戳回复\n使用方法：戳一下bot就可以了喔~\n========\n鸣谢名单：方长 给予功能实现方向")

# 戳一戳
def _poke_check(event:PokeNotifyEvent):
    return event.target_id==event.self_id
    
poke = on_notice(rule=_poke_check,priority=100)

# 预设方案①
preset_1 = [
    ("MISS", 0.2),
    ("GOOD", 0.2),
    ("GREAT", 0.5),
    ("PERFECT", 0.4),
    ("CRITICAL PERFECT", 0.2)
]

# 预设方案②
preset_2 = [
    ("嗝~绝赞都被我吃完惹！MISS！", 0.2),
    ("绝赞都快要吃完了，你怎么才来拍我……只能给你 GOOD 惹", 0.2),
    ("才吃一半，爆个粉，给你个 GREAT 吧~", 0.5),
    ("还没有吃掉绝赞，你抓住了Break，就给你 PERFECT 吧！", 0.4),
    ("还没看见绝赞，就被你抓走了……给你 CRITICAL PERFECT 的评价~！", 0.2)
]

# 使用预设方案
selected_preset = 2  # 修改这个值以选择不同的预设方案（1, 2, 3）

# 根据选择的预设方案设置消息列表
if selected_preset == 1:
    message_list = preset_1
elif selected_preset == 2:
    message_list = preset_2
else:
    message_list = preset_2  # 默认使用预设方案②

@poke.handle()
async def handle_poke(bot: Bot, event: PokeNotifyEvent):
    # 确认是戳机器人自己
    if event.target_id == event.self_id:
        # 分离消息和概率
        messages, weights = zip(*message_list)
        # 根据概率选一个消息回复
        reply = random.choices(messages, weights=weights, k=1)[0]
        await poke.send(reply)


