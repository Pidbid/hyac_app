# -*- encoding: utf-8 -*-
"""
@File    :   func.py
@Time    :   2023/01/08 00:33:41
@Author  :   Wicos 
@Version :   1.0
@Contact :   wicos@wicos.cn
@Blog    :   https://www.wicos.me
@Desc    :   控制函数与数据库的交互
"""

# here put the import lib
from functools import wraps
import asyncio
# class FUNC:
#     def __init__(self,appid:str):
#         self.appid = appid

#     def fun_add(self,name:str,code:str,tags:list,desc:str):
#         pass

#     def fun_update(self,name:str,code:str,tage:list,desc:str):
#         pass

#     def fun_delete(self,name:str):
#         pass

#     def fun_get(self,name:str):
#         pass


def pidbid_route(f):
    @wraps(f)
    async def decorated(*args, **kwargs):
        eval("print('你好')")
        return await f(*args, **kwargs)
    return decorated


@pidbid_route
async def func():
    return print("Function is running")

can_run = False

# print(func())
if __name__ =="__main__":
    fun = func()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    task = loop.create_task(fun)
    loop.run_until_complete(task)