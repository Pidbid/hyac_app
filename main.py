# -*- encoding: utf-8 -*-
"""
@File    :   main.py
@Time    :   2023/01/07 18:52:35
@Author  :   Wicos 
@Version :   1.0
@Contact :   wicos@wicos.cn
@Blog    :   https://www.wicos.me
"""

# here put the import lib
from fastapi import APIRouter, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from functools import wraps
from modelsconfig import CONFIG
from modelsdb import DB


db = DB()
app = FastAPI()
config = CONFIG()


# 跨域配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=db.app_cors["origins"],
    allow_credentials=db.app_cors["cookies"],
    allow_methods=db.app_cors["methods"],
    allow_headers=db.app_cors["headers"],
)

# route defined and include
app_routes = db.get_routes()
app_funcs = db.get_funcs()
# print([i for i in app_routes])
app_routes = [i for i in app_routes]

route_name = ""
parent_route_name = ""
route_method = ""
route_path = ""

# define routes
for route in app_routes:
    if route["type"] != "route":
        continue
    # route_name = "{}_route_{}".format(config.appid, route["routeid"])
    route_name = "{}_route_{}".format(config.appid, route["routeid"])
    exec_code = "{} = APIRouter()".format(route_name)
    exec(exec_code, globals())

# function route binding
for route in app_routes:
    parent_route_name = "{}_route_{}".format(config.appid, route["parentid"])
    fun_method = route["method"]
    fun_route = route["route"]
    if len(route["funcs"]) != 0:
        func_code = ""
        for f in app_funcs:
            if f["id"] in route["funcs"]:
                func_code = f["code"]
        incode = """def pidbid_route(f):\n    @{}.{}('{}')\n    @wraps(f)\n    async def decorated(*args, **kwargs):\n        return await f(*args, **kwargs)\n    return decorated
        """.format(
            parent_route_name, fun_method, fun_route
        )
        exec_bind_code = "{}\n\n{}".format(incode, func_code)
        exec(exec_bind_code, globals())


# include routes
for route in app_routes:
    if route["type"] != "route":
        continue
    route_name = "{}_route_{}".format(config.appid, route["routeid"])
    exec_code = ""
    if route["root_path"]:
        exec_code = "app.include_router({},prefix='{}')".format(
            route_name, route["route"]
        )
        # print(exec_code)
    else:
        parent_route_name = "{}_route_{}".format(config.appid, route["parentid"])
        exec_code = "{}.include_router({},prefix='{}')".format(
            parent_route_name, route_name, route["route"]
        )
        # print(exec_code)
    exec(exec_code, globals())


# if __name__ == "__main__":
#     print(globals())
#     uvicorn.run(app, host=config.host, port=config.port)
