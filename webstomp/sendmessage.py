# -*- coding: utf-8 -*- 

import pika
import json
import cmd
from sampledata import DATA_ATTACK


class MyTester(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "> "    # define command prompt
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.exchanger = 'situation'
        self.default_routing_key = 'ipflow'
        self.mq_init()

    def mq_init(self):
        self.channel.exchange_declare(exchange=self.exchanger,
                         type='fanout')

    def mq_send(self, message, rk=None):
        if not rk:
            rk = self.default_routing_key
        self.channel.basic_publish(exchange=self.exchanger,
                          routing_key=rk,
                          body=json.dumps(message))

    def do_send(self, arg):
        """
        发送测试数据：
        arg 待发送的数据
        """
        self.mq_send(arg)
        print '[OK] Sent', arg , '.'

    def do_send2(self, arg):
        """
        发送测试数据（到另一条routing_key）
        arg 待发送的数据
        """
        self.mq_send(arg,"anotherflow")
        print '[OK] Sent2', arg ,'.'

    def do_attack(self, arg):
        """
        发送模拟攻击数据：
        arg  0-2  代表不同的攻击数据包
        """
        self.mq_send(DATA_ATTACK[int(arg)])
        print '[OK] Data sent.'

    def do_exit(self, arg):
        self.connection.close()
        exit()


if __name__ == '__main__':
	tester = MyTester()
	tester.cmdloop()
