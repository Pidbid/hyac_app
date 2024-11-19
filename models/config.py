# -*- encoding: utf-8 -*-
"""
@File    :   config.py
@Time    :   2023/01/08 00:45:08
@Author  :   Wicos 
@Version :   1.0
@Contact :   wicos@wicos.cn
@Blog    :   https://www.wicos.me
"""

# here put the import lib
import os
import json

class CONFIG:
    def __init__(self):
        self.path_init()
        self.config_main = json.load(open(self.config_main_path, "r"))
        self.development = self.config_main["development"]
        self.config_init()
        self.main_init()
        self.db_init()
        self.token_init()
        self.app_init()

    def config_init(self):
        config_data = {}
        if self.development:
            with open(self.config_path, "r") as fp:
                config_lines = fp.readlines()
                for i in config_lines:
                    i = i.replace("\n","")
                    config_line = i.split("=")
                    config_data.update({config_line[0]: config_line[1]})
            self.config = config_data
        else:
            self.config = dict(os.environ)
    
    def app_init(self):
        self.appid = self.config["PB_APPID"]

    def path_init(self):
        if os.name == "nt":
            self.config_path = "{}\\.env.template".format(os.getcwd())
            self.config_main_path = "{}\\config.json".format(os.getcwd())
        else:
            self.config_path = "{}/.env.template".format(os.getcwd())
            self.config_main_path = "{}/config.json".format(os.getcwd())

    def main_init(self):
        self.host = self.config_main["host"]
        self.port = self.config_main["port"]
        self.reload = self.config_main["reload"]

    def db_init(self):
        self.db_uri = self.config["PB_DB_SYS_URI"]
        self.db_app_uri = self.config["PB_DB_APP_URI"]

    def token_init(self):
        self.token_salt = self.config_main["token_salt"]

