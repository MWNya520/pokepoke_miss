from nonebot import on_notice
from nonebot.adapters.onebot.v11 import PokeNotifyEvent, Bot, Event
from nonebot.plugin import PluginMetadata

import random

print("pokepoke_miss is running!")

# 戳一戳 Matcher
poke = on_notice(block=True)

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

# 预设方案③
# 火热更新中！
'''
message_list = [
    ("每次都差那么一点点，心态已经彻底崩溃了，手指也跟不上！",0.2),
    ("fast和slow简直是我的噩梦，心态已经炸裂，每次都差那么一点！",0.2),
    ("顶级谱面简直是在折磨人，手指都废了，脑子也跟不上了，绝望！",0.2),
    ("连打和滑条结合操作，简直是噩梦组合，手指和脑子都废了！",0.2),
    ("又是miss，我怀疑我的手指是不是出故障了，感觉自己在梦游！",0.2),
    ("每次都miss，心态已经炸裂，手指也残了，这游戏真的是魔鬼！",0.2),
    ("激光条真的太难了，眼睛都花了，手指跟不上，心态彻底崩了！",0.2),
    ("激光条加速操作，手指都快飞了，脑子也死机了，完全跟不上！",0.2),
    ("连打到手指抽筋，滑条到脑子死机，全是miss，彻底崩溃了！",0.2),
    ("这难度设定是给神仙打的吧，人类根本不可能打过，心态崩了！",0.2)
]
'''

@poke.handle()
async def handle_poke(bot: Bot, event: PokeNotifyEvent):
    # 确认是戳机器人自己
    if event.target_id == event.self_id:
        # 分离消息和概率
        messages, weights = zip(*message_list)
        # 根据概率选一个消息回复
        reply = random.choices(messages, weights=weights, k=1)[0]
        await poke.send(reply)
