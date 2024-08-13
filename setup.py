from setuptools import setup, find_packages

setup(
    name="pokepoke_miss",
    version="0.1.4",
    author="Miaowing",
    author_email="shengwang52005@163.com",
    description="wmc的戳一戳回复插件，消息内容、概率都可以定制喔~",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/shengwang52005/pokepoke_miss",
    packages=find_packages(),
    install_requires=[
        "nonebot2>=2.0.0",
        "nonebot-adapter-onebot>=2.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Nonebot2",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.7",
)
