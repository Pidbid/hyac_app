# -*- encoding: utf-8 -*-
"""
@File    :   funs.py
@Time    :   2023/01/11 18:33:41
@Author  :   Wicos 
@Version :   1.0
@Contact :   wicos@wicos.cn
@Blog    :   https://www.wicos.me
@Desc    :   common functions
"""

# here put the import lib
from modules.config import CONFIG

config = CONFIG()


def route_init(route:dict):
    if route["root_route"]:
        exec_code = "{}_route_{} = APIRouter()".format(config.appid, route["routeid"])
        exec(exec_code)
    else:
        exec_code = "{}_route_{} = APIRouter()".format(config.appid, route["routeid"])
        exec(exec_code)
    
