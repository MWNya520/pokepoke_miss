import nonebot

from nonebot.plugin import PluginMetadata
from pathlib import Path

from . import __main__

# 插件信息
__plugin_meta__ = PluginMetadata(
    name="pokepoke_miss",
    description="wmc的戳一戳回复插件，消息内容、概率都可以定制喔~",
    usage="戳一戳",
    type="application",
    homepage="https://github.com/shengwang52005/pokepoke_miss",
    supported_adapters={"~onebot.v11"},
)