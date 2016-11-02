# -*- coding: utf-8 -*- 
DATA_ATTACK = [
                {"src_ip":"10.10.0.5",          #源IP地址
                 "src_port":25431,              #源端口号
                 "dest_ip":"10.20.0.4",         #目的IP地址
                 "dest_port":80,                #目的端口号
                 "attack_type":"SQL_INJECTION", #攻击类型
                 "intercepted": False,          #是否被拦截
                 "captured": False              #目标是否攻占
                 },


                {"src_ip":"10.10.0.5",
                 "src_port":25431,
                 "dest_ip":"10.20.0.4",
                 "dest_port":80,
                 "attack_type":"SQL_INJECTION",
                 "intercepted": True,
                 "captured": False
                 },


                {"src_ip":"10.10.0.5",
                 "src_port":25431,
                 "dest_ip":"10.20.0.4",
                 "dest_port":80,
                 "attack_type":"SQL_INJECTION",
                 "intercepted": False,
                 "captured": True
                 }
                ]

