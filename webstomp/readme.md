# RabbitMQ Websocket调用示例

## 准备工作

- 安装RabbitMQ（之前需要安装Erlang）。
- 启用RabbitMQ的web stomp插件。

```
rabbitmq-plugins enable rabbitmq_web_stomp
```

## 测试系统

- 打开webstomp_ws.html
- 启动sendmessage.py


```
python sendmessage.py

>send hello world
[OK] Sent hello world.

>attack 0
[OK] Data sent.

>attack 1
[OK] Data sent.

>attack 2
[OK] Data sent.

#使用另一个routing key
> send2 test
[OK] Sent2 test .
```