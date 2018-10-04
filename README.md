# python-chatting
2018.10: 最近我在学rust。我对它很感兴趣，以至于我决定要用rust写完这个未完成的项目。但未来的空闲时间不多了，我不知道要什么时候能完成这个项目。

对了，```network```文件夹里面的都是乱写的。

[English Ver.](./readme_.md)
~~~有点丢脸，别看了~~~

---
这是一个基于flask的聊天应用。

我的运行环境：
```
Ubuntu 18.04 LTS
Python 3.6.5
```

# 目标
* 验证用户的登录（但其具体的方式尚不明确）
* 使用p2p网络传递信息
* 加密发送的和接收的信息
* 创建一个简单的聊天机器人[2018.9.14 增加了一个简单的机器人]

 ~~路漫漫其修远兮~~

# 安装
```
$ git clone git@github.com:ceontouwong/python-chatting.git
$ pip3 install -r requirements.txt
```
或
```
$ git clone git@github.com:ceontouwong/python-chatting.git
$ pip install -r requirements.txt
```

# 运行
运行根目录下的```main.py```后，进入```127.0.0.1:5000```即可使用。
