# -*- encoding: utf-8 -*-
"""
@File    :   db.py
@Time    :   2023/01/08 00:39:11
@Author  :   Wicos 
@Version :   1.0
@Contact :   wicos@wicos.cn
@Blog    :   https://www.wicos.me
"""

# here put the import lib
import pymongo
from models.config import CONFIG

config = CONFIG()


class DB:
    def __init__(self):
        self.client_main = pymongo.MongoClient(config.db_uri)
        self.client = pymongo.MongoClient(config.db_app_uri)
        self.db_init()
        self.get_cors()
        # self.get_funcs()

    def db_init(self):
        # 总数据库
        self.db_main = self.client_main.pidbid
        # 应用数据库
        self.db = self.client["app_{}".format(config.appid)]

    def get_cors(self):
        self.app_cors = self.db_main["sys-apps-setting"].find_one(
            {"appid": config.appid}
        )["cors"]

    def get_routes(self):
        # self.app_route = self.db_main["sys-apps-route"].find({"appid":config.appid})
        return self.db_main["sys-apps-route"].aggregate(
            [{"$match": {"appid": config.appid}}, {"$sort": {"depth": -1}}]
        )
        # print([i for i in self.app_route])
        # self.app_route_root = []
        # self.app_route_child = []
        # for route in self.app_route:
        #     if route["root_path"]:
        #         self.app_route_root.append(route)
        #     else:
        #         self.app_route_child.append(route)

    def get_funcs(self):
        self.app_funcs = self.db_main["sys-apps-function"].find({"appid": config.appid})
        return [i for i in self.app_funcs]
        # print([i for i in self.app_funcs])

    def get_func(self, funcid: str):
        return self.db_main["sys-apps-function"].find_one(
            {"appid": config.appid, "functionid": funcid}
        )
