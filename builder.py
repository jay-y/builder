#! /usr/bin/env python
# coding: utf-8

import os
import json
import shutil
from logger import Logger


class Builder:
    def __init__(self):
        self.const_config = None
        self.logger = Logger()

    def read_config(self):  # 读取配置
        if None == self.const_config:
            config_path = 'config.json'
            if os.path.exists(config_path):
                with open(config_path) as fp:
                    self.const_config = json.load(fp)
                    return self.const_config
            else:
                self.logger.error("找不到配置文件")
        else:
            return self.const_config

    def proc(self, config):  # 处理
        read = config["read_path"]  # 源文件目录
        out = config["out_path"]  # 输出目录
        cts = config["create"]
        cps = config["copy"]
        if not os.path.exists(out):  # 输出目录不存在时创建目录
            self.logger.warn("输出目录不存在")
            self.proc_create(out)
        self.logger.info("输出目录清理...")
        shutil.rmtree(out, True)
        self.logger.info("输出目录清理完成")
        if os.path.exists(read):
            self.logger.info("读取源目录...")
            ## 文件创建处理 ##
            for ct in cts:
                name = ct["name"]
                path = out + name
                is_file = ct["is_file"]
                if is_file:
                    content = ct["content"]
                    self.proc_create(path, is_file, content)
                else:
                    self.proc_create(path)
            ## 文件拷贝处理 ##
            for cp in cps:
                old_path = read + cp["old_path"]
                new_path = out + cp["new_path"]
                self.proc_copy(old_path, new_path)
            return True
        else:
            self.logger.error("源目录不存在")
            return False

    def proc_create(self, path, is_file=False, content=""):
        if is_file is True:
            f = open(path, "w+")
            f.write(content.encode("utf-8"))
            f.close()
        else:
            os.makedirs(path)
        self.logger.info("CREATE: {}".format(path))

    def proc_copy(self, old_path, new_path):
        if os.path.exists(old_path):
            if os.path.isdir(old_path):
                shutil.copytree(old_path, new_path)
            elif os.path.isfile(old_path):
                shutil.copy(old_path, new_path)
            self.logger.info("COPY: {} -> {}".format(old_path, new_path))
        else:
            self.logger.error("NOT FOUND: {}".format(old_path))

    def run(self):
        self.logger.info("配置文件读取...")
        s = self.read_config()
        self.logger.info("配置文件读取完成")
        b = self.proc(s)
        if b:
            self.logger.info("构建完成")
        else:
            self.logger.info("构建失败")
