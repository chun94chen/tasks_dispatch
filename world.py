# -*- coding:utf-8 -*-
from dingtalk import DingTalkApp
from datetime import datetime
import redis

# 使用redis管理钉钉会话
session_manager = redis.Redis(host='127.0.0.1', password='dana', port='6379', db=0, decode_responses=True)
dd_app = DingTalkApp(name='stdt', session_manager=session_manager,
                         agent_id='229744920',
                         corp_id='dingy90qtakvip9ucl7m',
                         corp_secret='Khzk-MQ7eoiVJIf6bl21Za8wT-phMd7mU0ZSwfsQHntYJgOUPMz0fVhQsr05oQbT',
                         aes_key='4g5j64qlyl3zvetqxz5jiocdr586fn2zvjpa8zls3ji')


# 获取钉钉后台定义的外部联系人标签
label_groups = dd_app.customer.get_label_groups()
print(label_groups)
# 获取审批实例
# start_time = datetime(year=2017, month=6, day=1, hour=1, minute=1, second=1, microsecond=1)
# 以下皆是模拟数据
# print(dd_app.contact.get_all_org_users())
