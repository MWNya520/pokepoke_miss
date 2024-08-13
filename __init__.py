from nonebot.plugin import PluginMetadata

from .pokepoke_miss import *


# 插件元数据
__plugin_meta__ = PluginMetadata(
    name="pokepoke_miss",
    description="wmc的戳一戳回复插件，消息内容、概率都可以定制喔~",
    usage="戳一戳回复，提供娱乐功能",
    type="application",
    extra={},
)